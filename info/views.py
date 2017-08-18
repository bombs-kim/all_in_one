from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import esm
from .forms import SearchForm

def add_site_info(orders, site):
    for order in orders:
        order['site__'] = site

def get_entries(account, stage, start=None, end=None,
                 searchKey='ON', searchKeyword=''):
    if account.site in ('ESM', 'GMKT', 'AUC'):
        handlers = {
            "neworder": esm.get_neworder,
            "todeliver": esm.get_todeliver,
            "sending": esm.get_sending
        }
        if stage not in handlers:
            print("Error")
            return
        mID, entries = handlers[stage](
            account.userid, account.password, account.site,
            start, end, searchKey, searchKeyword)
        entries = entries['data']
        for entry in entries:
            entry['mID'] = mID
            entry['orderInfo'] = ",".join(str(e) for e in
                (entry['OrderNo'], entry['SiteIDValue'], entry['SellerCustNo']))
        add_site_info(entries, account.site)
        return entries
    # To do: Other malls

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
                new_entries = get_entries(account, stage, start,
                                       end, option, keyword)
    else:
        search_form = SearchForm()
        for account in accounts:
            entries += get_entries(account, stage)
    return search_form, entries


@login_required
def neworders(request):
    accounts = request.user.master.accounts.all()
    search_form, neworders = get_form_and_entries(
        request, accounts, "neworder")
    return render(request,
                  'info/neworders.html',
                  {'neworders': neworders,
                   'search_form': search_form})

@login_required
def todeliver(request):
    accounts = request.user.master.accounts.all()
    search_form, neworders = get_form_and_entries(
        request, accounts, "todeliver")
    return render(request,
                  'info/neworders.html',
                  {'neworders': neworders,
                   'search_form': search_form})


@login_required
def sending(request):
    pass
