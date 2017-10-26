import json
from collections import defaultdict
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.utils import timezone
from pprint import pprint
from . import esm, storefarm, cafe24
from .forms import SearchForm
from master.models import Master


from datetime import datetime
import pytz
tz = pytz.timezone("Asia/Seoul")


def attach_meta_info(entries, account):
    for entry in entries:
        entry['site__'] = account.site
        entry['userid__'] = account.userid


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
        entries = esm.search(
            account, stage,
            start, end, searchKey, searchKeyword)
        # Attach datetime__ attribute that would be used as the sorting criteria
        # get_form_and_entries function will use that attribute. Note that
        # sorting entries based on some datetime attribute is still experimental
        # and there are many cadidate times that could be used to sort entries.
        # ex) Order date vs Deliver date
        esm.attach_local_datetime(entries, tz)
    elif account.site == "STOREFARM":
        entries = storefarm.search(
            account, stage,
            start, end, searchKey, searchKeyword)
        storefarm.attach_local_datetime(entries, tz, stage)
    elif account.site == "CAFE24":
        entries = cafe24.search(
            account, stage,
            start, end, searchKey, searchKeyword)
        cafe24.attach_local_datetime(entries, tz)
    attach_meta_info(entries, account)
    return entries


# Getting a form and getting entries are two different tasks. But we cannot
# separte those two tasks and write a different function for each because
# they are dependent.
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
    entries.sort(key=lambda a: a['datetime__'])
    return search_form, entries


@login_required
def neworder(request):
    accounts = request.user.master.accounts.all()
    search_form, entries = get_form_and_entries(
        request, accounts, "neworder")
    return render(request,
                  'info/neworder.html',
                  {'entries': entries,
                   'search_form': search_form})


@login_required
def deliver(request):
    accounts = request.user.master.accounts.all()
    search_form, entries = get_form_and_entries(
        request, accounts, "deliver")
    return render(request,
                  'info/deliver.html',
                  {'entries': entries,
                   'search_form': search_form})


@login_required
def deliverstatus(request):
    accounts = request.user.master.accounts.all()
    search_form, entries = get_form_and_entries(
        request, accounts, "deliverstatus")
    return render(request,
                  'info/deliverstatus.html',
                  {'entries': entries,
                   'search_form': search_form})

@login_required
def cancel(request):
    accounts = request.user.master.accounts.all()
    search_form, entries = get_form_and_entries(
        request, accounts, "cancel")
    return render(request,
                  'info/cancel.html',
                  {'entries': entries,
                   'search_form': search_form})

@login_required
def refund(request):
    accounts = request.user.master.accounts.all()
    search_form, entries = get_form_and_entries(
        request, accounts, "refund")
    return render(request,
                  'info/refund.html',
                  {'entries': entries,
                   'search_form': search_form})

@login_required
def exchange(request):
    accounts = request.user.master.accounts.all()
    search_form, entries = get_form_and_entries(
        request, accounts, "exchange")
    return render(request,
                  'info/exchange.html',
                  {'entries': entries,
                   'search_form': search_form})

@login_required
@require_POST
def neworder_confirm(request):
    orders = request.POST.getlist('orderInfo')

    ESM_orders = defaultdict(list)
    STOREFARM_orders = defaultdict(list)
    CAFE24_orders = defaultdict(list)

    for order in orders:
        site, seller_id, order_info = order.split("/")
        if site == "ESM":
            ESM_orders[seller_id].append(order_info)
        elif site == "STOREFARM":
            STOREFARM_orders[seller_id].append(order_info)
        elif site == "CAFE24":
            CAFE24_orders[seller_id].append(order_info)

    accounts = request.user.master.accounts.all()

    for seller_id in ESM_orders:
        account = accounts.get(userid=seller_id)
        # ex) "2008008812,2,111421746^2004109789,2,111421746"
        order_info = "^".join(ESM_orders[seller_id])
        resp = esm.neworder_confirm(
            account.userid, account.password,
            account.site, order_info)
        # Do nothing with resp currently

    for seller_id in STOREFARM_orders:
        account = accounts.get(userid=seller_id)
        order_info = ",".join(STOREFARM_orders[seller_id])
        resp = storefarm.neworder_confirm(
            account, order_info)
        # Do nothing with resp currently

    for seller_id in CAFE24_orders:
        account = accounts.get(userid=seller_id)
        resp = cafe24.neworder_confirm(
            account, CAFE24_orders[seller_id])
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
def deliver_confirm(request):
    orders = request.POST.getlist('orderInfo')
    comps = request.POST.getlist('company')
    invs = request.POST.getlist('invoiceNo')

    ESM_orders = defaultdict(list)
    STOREFARM_orders = defaultdict(list)
    CAFE24_orders = defaultdict(list)

    for idx, order in enumerate(orders):
        site, seller_id, order_number = order.split("/")
        if site == "ESM":
            ESM_orders[seller_id].append(
                order_number + "," +
                comps[idx] + "," +
                companies[comps[idx]] + "," +
                invs[idx]  )
        elif site == "STOREFARM":
            STOREFARM_orders[seller_id].append(
                # tuple type
                (order_number, comps[idx], invs[idx])  )
        elif site == "CAFE24":
            CAFE24_orders[seller_id].append(
                (order_number, comps[idx], invs[idx])  )

    accounts = request.user.master.accounts.all()
    success = True
    for seller_id in ESM_orders:
        account = accounts.get(userid=seller_id)
        # order_info format: order_number,company_num,company,invoice
        # ex) 2008278271,10013,CJ택배,1234567890^2008278271,10013,CJ택배,1234567890
        order_info = '^'.join(ESM_orders[seller_id])
        resp = esm.deliver_confirm(
            account.userid, account.password,
            account.site, order_info)
        # example response
        # {'message': '1건이 발송처리 되었습니다.\r\n1건이 발송처리중 오류가 발생했습니다.', 'success': True}
        # note that 'success' value is still True!
        j = json.loads(resp.text)
                              # string based failure test. vulnerable to change in the future
        if not j['success'] or '오류' in j['message'] :
            success = False
        msg = j['message'] + '\n'

    for seller_id in STOREFARM_orders:
        account = accounts.get(userid=seller_id)
        resp = storefarm.deliver_confirm(
            account,
            STOREFARM_orders[seller_id])
        try:
            j = json.loads(resp.text)
            if not j['bSuccess']:
                success = False
                msg = j['htReturnValue']['results'][-1]['message']  + '\n'
        except:
            success = False
            msg = resp.text

    for seller_id in CAFE24_orders:
        account = accounts.get(userid=seller_id)
        resp = cafe24.deliver_confirm(
            account,
            CAFE24_orders[seller_id])
        msg = resp.text

    if not success:
        return JsonResponse({'status': 'fail', 'msg': msg})
    return JsonResponse({'status':'ok', 'msg': msg})


# 취소 확정
@login_required
@require_POST
def cancel_confirm(request):
    site, seller_id, order_info = request.POST['orderInfo'].split("/")
    accounts = request.user.master.accounts.all()
    account = accounts.get(site=site, userid=seller_id)
    success = True
    msg = ''
    if site == 'ESM':
        # result is str type
        result = esm.cancel_confirm(account, order_info)
        msg = order_info + ': '
        if "실패" in result :
            success = False
        msg += result
    elif site == 'STOREFARM':
        resp = storefarm.cancel_confirm(
            account, order_info)
    elif site == 'CAFE24':
        cafe24.cancel_confirm(account, order_info)
    if not success:
        return JsonResponse({'status': 'fail', 'msg': msg})
    return JsonResponse({'status':'ok', 'msg': msg})


# 취소 반려 및 배송처리
@login_required
@require_POST
def cancel_deliver(request):
    site, seller_id, order_info = request.POST['orderInfo'].split("/")
    order_info = order_info.rsplit(',', 2)[0]
    comp = request.POST['deliveryComp']  # 택배회사코드
    comp_name = request.POST.get('deliveryCompanyName')
    inv = request.POST['invoiceNo']

    accounts = request.user.master.accounts.all()
    account = accounts.get(site=site, userid=seller_id)
    msg = order_info + ': '
    if site == 'ESM':
        success = True
        # result is str type
        result = esm.cancel_deliver(account,
              order_info, comp, comp_name,inv)
        if "실패" in result :
            success = False
        msg += result
    elif site == 'STOREFARM':
        success = False
        resp = storefarm.cancel_deliver(
            account, order_info, comp, inv)
        try:
            j = json.loads(resp.text)
            if j['bSuccess']:
                success = True
        except:
            pass
        msg += resp.text
    else:
        success = False
        msg += "Not implemented"
    if not success:
        return JsonResponse({'status': 'fail', 'msg': msg})
    return JsonResponse({'status':'ok', 'msg': msg})


# 수거완료 처리(스토어팜 전용)
@login_required
@require_POST
def refund_collect_done(request):
    site, seller_id, order_info = request.POST['orderInfo'].split("/")
    accounts = request.user.master.accounts.all()
    account = accounts.get(userid=seller_id)
    if not "STOREFARM" in site:
        return JsonResponse({'status': 'fail',
             'msg': "스토어팜 제품만 수거완료 처리가 가능합니다"})
    success = False
    resp = storefarm.refund_collect_done(account, order_info)
    try:
        j = json.loads(resp.text)
        if j['bSuccess']:
            success = True
    except:
        pass
    msg = order_info + ': ' + resp.text
    if not success:
        return JsonResponse({'status':'fail', 'msg': msg})
    return JsonResponse({'status':'ok', 'msg': msg})


@login_required
@require_POST
def refund_confirm(request):
    site, seller_id, order_info = request.POST['orderInfo'].split("/")
    accounts = request.user.master.accounts.all()
    account = accounts.get(userid=seller_id)
    success = True
    if site == 'ESM':
        # result example
        # {'message': '환불 승인되었습니다.', 'success': True}
        result = esm.refund_confirm(
            account.userid, account.password,
            account.site, order_info)
        msg = order_info + ': ' + result['message']
                # string based failure test. vulnerable to changes in the future
        if not result['success'] or "오류" in result["message"] :
            success = False
    elif "STOREFARM" in site:
        siccess = False
        resp = storefarm.refund_confirm(account, order_info)
        msg = order_info + ':\n' + resp.text
        try:
            j = json.loads(resp.text)
            if j['bSuccess']:
                success = True
        except:
            pass
    elif site == "CAFE24":
        cafe24.refund_confirm(account, order_info)
        msg = ''
    if not success:
        return JsonResponse({'status': 'fail', 'msg': msg})
    return JsonResponse({'status':'ok', 'msg': msg})


@login_required
@require_POST
def exchange_collect_done(request):
    site, seller_id, order_info = request.POST['orderInfo'].split("/")
    accounts = request.user.master.accounts.all()
    account = accounts.get(userid=seller_id)
    if not "STOREFARM" in site:
        return JsonResponse({'status': 'fail',
             'msg': "스토어팜 제품만 수거완료 처리가 가능합니다"})
    success = False
    resp = storefarm.exchange_collect_done(account, order_info)
    try:
        j = json.loads(resp.text)
        if j['bSuccess']:
            success = True
    except:
        pass
    msg = order_info + ': ' + resp.text
    if not success:
        return JsonResponse({'status':'fail', 'msg': msg})
    return JsonResponse({'status':'ok', 'msg': msg})



@login_required
@require_POST
def exchange_confirm(request):
    site, seller_id, order_info = request.POST['orderInfo'].split("/")
    comp = request.POST.get('resendCompCode')  # 택배회사코드
    inv = request.POST.get('invoiceNo')

    accounts = request.user.master.accounts.all()
    account = accounts.get(userid=seller_id)
    success = True
    if site == 'ESM':
        # result example
        # {'message': '재발송 처리되었습니다. \n\n
        #  교환 재발송 처리된 주문건은 배송중 메뉴에서 확인하시기 바랍니다.',
        #  'success': True}
        result = esm.exchange_confirm(
            account.userid, account.password, account.site,
            order_info, comp, inv)
        msg = order_info + ':\n'
                # string based failure test. vulnerable to changes in the future
        if not result['success'] or "오류" in result["message"] :
            success = False
        msg += result['message']
    elif "STOREFARM" in site:
        success = False
        resp = storefarm.exchange_confirm(account, order_info, comp, inv)
        msg = order_info + ':\n' + resp.text
        try:
            j = json.loads(resp.text)
            if j['bSuccess']:
                success = True
        except:
            pass
    elif site == "CAFE24":
        cafe24.exchange_confirm(account, order_info)
        msg = ''
    if not success:
        return JsonResponse({'status': 'fail', 'msg': msg})
    return JsonResponse({'status':'ok', 'msg': msg})
