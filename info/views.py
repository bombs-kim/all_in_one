import json
import requests
from collections import defaultdict
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from pprint import pprint
from . import esm
from .forms import SearchForm
from master.models import Master


def add_extra_info(entries, site):
    for entry in entries:
        entry['site__'] = site


def get_entries(account, stage, start=None, end=None,
                 searchKey='ON', searchKeyword=''):
    if account.site in ('ESM', 'GMKT', 'AUC'):
        # handlers = {
        #     "neworder": esm.get_neworder,
        #     "todeliver": esm.get_todeliver,
        #     "sending": esm.get_sending
        # }
        # if stage not in handlers:
        #     print("Error")
        #     return
        mID, entries = esm.search(
            account.userid, account.password, stage, account.site,
            start, end, searchKey, searchKeyword)
        entries = entries['data']

        # add ESM specific info
        for entry in entries:
            entry['mID'] = mID
            if stage == "neworder":
                entry['orderInfo'] = ",".join(str(e) for e in
                    (entry['OrderNo'],
                     entry['SiteIDValue'],
                     entry['SellerCustNo'])
                    )

        # To do: Other malls
    add_extra_info(entries, account.site)
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

def toreturn(request):
    accounts = request.user.master.accounts.all()
    search_form, entries = get_form_and_entries(
        request, accounts, "toreturn")
    return render(request,
                  'info/toreturn.html',
                  {'entries': entries,
                   'search_form': search_form})

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
