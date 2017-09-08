import json
import requests
from collections import defaultdict
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.utils import timezone
from pprint import pprint
from . import esm, storefarm
from .forms import SearchForm
from master.models import Master


def add_extra_info(entries, account):
    for entry in entries:
        entry['site__'] = account.site
        entry['userid__'] = account.userid

# Special case for ESM exchange
# This is needed if you need to search on multiple status at the same time
# def ESM_exchange_search(account_userid, account_password, stage, account_site,
#                         start, end, searchKey, searchKeyword):
#     total_entries = []
#     for searchStatus in ("EP",):
#         mID, entries = esm.search(
#             account_userid, account_password, stage, account_site,
#             start, end, searchKey, searchKeyword, searchStatus)
#         pprint(type(entries))
#         total_entries += entries['data']
#     return mID, {'data': total_entries}


from datetime import datetime
import pytz
tz = pytz.timezone("Asia/Seoul")
def fromtimestamp(epoch):
    return datetime.fromtimestamp(1504148557, tz=tz)


def get_entries(account, stage, start=None, end=None,
                 searchKey='ON', searchKeyword=''):
    # start, end: datetime.date type
    if not start:
        if end:
            print("Error")
            return
        start = (timezone.now()-timezone.timedelta(days=30)).date()
        end = timezone.now().date()

    if account.site in ('ESM', 'GMKT', 'AUC'):
        # search = ESM_exchange_search if stage == "toexchange" else esm.search
        entries = esm.search(
            account, stage,
            start, end, searchKey, searchKeyword)

        for entry in entries:
            # To be used as the sorting criteria
            dt = datetime.strptime(
                entry['DepositConfirmDate'], "%Y-%m-%d %H:%M:%S")
            entry['_datetime'] = tz.localize(dt)


    elif account.site == "STOREFARM":
        entries = storefarm.search(
            account.userid, account.password, stage, account.site,
            start, end, searchKey, searchKeyword)
        # entries = entries["htReturnValue"]["pagedResult"]["content"]
        for entry in entries:
            if stage == 'sending':
                dt1 = fromtimestamp(entry['PRODUCT_ORDER_PAY_YMDT'])
                # To be used as the sorting criteria
                entry['_datetime'] = dt1
                entry['PRODUCT_ORDER_PAY_YMDT'] = dt1.strftime('%Y-%m-%d %H:%M:%S')
                dt2 = fromtimestamp(entry['PRODUCT_ORDER_DISPATCH_OPERATION_YMDT'])
                entry['PRODUCT_ORDER_DISPATCH_OPERATION_YMDT'] =\
                                  dt2.strftime('%Y-%m-%d %H:%M:%S')
            else:
                dt = fromtimestamp(entry['PAY_PAY_YMDT'])
                # To be used as the sorting criteria
                entry['_datetime'] = dt
                entry['PAY_PAY_YMDT'] = dt.strftime('%Y-%m-%d %H:%M:%S')
                if stage == 'toreturn':
                    entry['CLAIM_REQUEST_OPERATION_YMDT_RETURN'] = fromtimestamp(
                        entry['CLAIM_REQUEST_OPERATION_YMDT_RETURN']
                        ).strftime('%Y-%m-%d %H:%M:%S')
                elif stage == 'toexchange':
                    entry['CLAIM_REQUEST_OPERATION_YMDT_EXCHANGE'] = fromtimestamp(
                        entry['CLAIM_REQUEST_OPERATION_YMDT_EXCHANGE']
                        ).strftime('%Y-%m-%d %H:%M:%S')
    add_extra_info(entries, account)
    return entries


def get_form_and_entries(request, accounts, stage):
    entries = []
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            cd = search_form.cleaned_data
            option = cd['search_option']
            keyword = cd['search_keyword']
            start = cd['start_date']
            end = cd['end_date']
            for account in accounts:
                entries += get_entries(account, stage, start,
                                       end, option, keyword)
    else:
        search_form = SearchForm()
        for account in accounts:
            entries += get_entries(account, stage)
    entries.sort(key=lambda a: a['_datetime'])
    return search_form, entries


@login_required
def neworder(request):
    accounts = request.user.master.accounts.all()
    search_form, entries = get_form_and_entries(
        request, accounts, "neworder")
    return render(request,
                  'info/neworders.html',
                  {'entries': entries,
                   'search_form': search_form})


@login_required
def todeliver(request):
    accounts = request.user.master.accounts.all()
    search_form, entries = get_form_and_entries(
        request, accounts, "todeliver")
    return render(request,
                  'info/todeliver.html',
                  {'entries': entries,
                   'search_form': search_form})


@login_required
def sending(request):
    accounts = request.user.master.accounts.all()
    search_form, entries = get_form_and_entries(
        request, accounts, "sending")
    return render(request,
                  'info/sending.html',
                  {'entries': entries,
                   'search_form': search_form})

@login_required
def tocancel(request):
    accounts = request.user.master.accounts.all()
    search_form, entries = get_form_and_entries(
        request, accounts, "tocancel")
    return render(request,
                  'info/tocancel.html',
                  {'entries': entries,
                   'search_form': search_form})

@login_required
def toreturn(request):
    accounts = request.user.master.accounts.all()
    search_form, entries = get_form_and_entries(
        request, accounts, "toreturn")
    return render(request,
                  'info/toreturn.html',
                  {'entries': entries,
                   'search_form': search_form})

@login_required
def toexchange(request):
    accounts = request.user.master.accounts.all()
    search_form, entries = get_form_and_entries(
        request, accounts, "toexchange")
    return render(request,
                  'info/toexchange.html',
                  {'entries': entries,
                   'search_form': search_form})

@login_required
@require_POST
def neworder_confirm(request):
    ESM_orders = defaultdict(list)
    orders = request.POST.getlist('orderInfo')

    for order in orders:
        site, seller_id, order_info = order.split("/")
        if site == "ESM":
            ESM_orders[seller_id].append(order_info)

    accounts = request.user.master.accounts.all()

    for seller_id in ESM_orders:
        account = accounts.get(userid=seller_id)
        # ex) "2008008812,2,111421746^2004109789,2,111421746"
        order_info = "^".join(ESM_orders[seller_id])
        resp = esm.neworder_confirm(
            account.userid, account.password,
            account.site, order_info)
        # Do nothing with resp currently
    return JsonResponse({'status':'ok'})

# ESM
companies = {
    "10013": "CJ택배",
    "10001": "대한통운",
    "10007": "한진택배",
    "10005": "우체국택배",
    "10008": "롯데택배",
    "10075": "롯데국제특송",
}

@login_required
@require_POST
def todeliver_confirm(request):
    ESM_orders = defaultdict(list)
    orders = request.POST.getlist('orderInfo')
    comp = request.POST.getlist('company')
    inv = request.POST.getlist('invoiceNo')

    for idx, order in enumerate(orders):
        site, seller_id, order_number = order.split("/")
        if site == "ESM":
            ESM_orders[seller_id].append(
                order_number + "," +
                comp[idx] + "," +
                companies[comp[idx]] + "," +
                inv[idx]
            )
    accounts = request.user.master.accounts.all()
    success = True
    msg = ""
    for seller_id in ESM_orders:
        account = accounts.get(userid=seller_id)
        # order_info format: order_number,company_num,company,invoice
        # ex) 2008278271,10013,CJ택배,1234567890^2008278271,10013,CJ택배,1234567890
        order_info = '^'.join(ESM_orders[seller_id])
        resp = esm.todeliver_confirm(
            account.userid, account.password,
            account.site, order_info)
        # example response
        # {'message': '1건이 발송처리 되었습니다.\r\n1건이 발송처리중 오류가 발생했습니다.', 'success': True}
        # note that 'success' value is still True!
        j = json.loads(resp.text)
                              # string based failure test. vulnerable to change in the future
        if not j['success'] or "오류" in j["message"] :
            success = False
        msg += j['message'] + "\n"
    if not success:
        return JsonResponse({'status': 'fail', 'msg': msg})
    return JsonResponse({'status':'ok', 'msg': msg})


@login_required
@require_POST
def tocancel_confirm(request):
    site, seller_id, order_info = request.POST['orderInfo'].split("/")
    accounts = request.user.master.accounts.all()
    account = accounts.get(site=site, userid=seller_id)
    success = True
    if site == 'ESM':
        # result is str type
        result = esm.tocancel_confirm(account, order_info)
        msg = order_info + ': '
        if "실패" in result :
            success = False
        msg += result
    else:
        print("Not implemented")
    if not success:
        return JsonResponse({'status': 'fail', 'msg': msg})
    return JsonResponse({'status':'ok', 'msg': msg})


    pass

@login_required
@require_POST
def tocancel_deliver(request):
    site, seller_id, order_info = request.POST['orderInfo'].split("/")
    order_info = order_info.rsplit(',', 2)[0]
    comp = request.POST['deliveryComp']  # 택배회사코드
    comp_name = request.POST['deliveryCompanyName']
    inv = request.POST['invoiceNo']

    accounts = request.user.master.accounts.all()
    account = accounts.get(site=site, userid=seller_id)
    success = True
    if site == 'ESM':
        # result is str type
        result = esm.tocancel_deliver(account,
              order_info, comp, comp_name,inv)
        msg = order_info + ': '
        if "실패" in result :
            success = False
        msg += result
    else:
        print("Not implemented")
    if not success:
        return JsonResponse({'status': 'fail', 'msg': msg})
    return JsonResponse({'status':'ok', 'msg': msg})

@login_required
@require_POST
def toreturn_confirm(request):
    site, seller_id, order_info = request.POST['orderInfo'].split("/")
    accounts = request.user.master.accounts.all()
    account = accounts.get(userid=seller_id)
    success = True
    if site == 'ESM':
        # result example
        # {'message': '환불 승인되었습니다.', 'success': True}
        result = esm.toreturn_confirm(
            account.userid, account.password,
            account.site, order_info)
        msg = order_info + ': '
                # string based failure test. vulnerable to changes in the future
        if not result['success'] or "오류" in result["message"] :
            success = False
        msg += result['message']
    else:
        print("Not implemented")
    if not success:
        return JsonResponse({'status': 'fail', 'msg': msg})
    return JsonResponse({'status':'ok', 'msg': msg})


@login_required
@require_POST
def toexchange_confirm(request):
    site, seller_id, order_info = request.POST['orderInfo'].split("/")
    comp = request.POST['resendCompCode']  # 택배회사코드
    inv = request.POST['invoiceNo']

    accounts = request.user.master.accounts.all()
    account = accounts.get(userid=seller_id)
    success = True
    if site == 'ESM':
        # result example
        # {'message': '재발송 처리되었습니다. \n\n
        #  교환 재발송 처리된 주문건은 배송중 메뉴에서 확인하시기 바랍니다.',
        #  'success': True}
        result = esm.toexchange_confirm(
            account.userid, account.password, account.site,
            order_info, comp, inv)
        msg = order_info + ': '
                # string based failure test. vulnerable to changes in the future
        if not result['success'] or "오류" in result["message"] :
            success = False
        msg += result['message']
    else:
        print("Not implemented")
    if not success:
        return JsonResponse({'status': 'fail', 'msg': msg})
    return JsonResponse({'status':'ok', 'msg': msg})
