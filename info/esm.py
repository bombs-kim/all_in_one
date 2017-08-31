import io
import json
import requests
import sys
from lxml.html import parse, submit_form
from pprint import pprint
from scrapy.selector import Selector
from django.utils import timezone

headers = {
    'Origin': 'https://www.esmplus.com',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8,ko;q=0.6',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    # 'Referer': 'https://www.esmplus.com/Member/SignIn/LogOn?ReturnValue=-7',
    'Connection': 'keep-alive',
    # 'X-Requested-With': 'XMLHttpRequest'
}

# Returns account number
def login(sess, id, pw, site):
    login_data = [
        ('Password', pw),
        ('ReturnUrl', ''),
        ('Id', id),
        ('RememberMe', 'true'),
        ('RememberMe', 'false'),
    ]
    if site == "ESM":
        login_data.append( ('Type', 'E') )
    else:
        login_data.append( ('Type', 'S') )
        if site == "GMKT":
            login_data.append( ('SiteType', 'GMKT') ) # G market
        else:
            login_data.append( ('SiteType', 'IAC') ) # Auction

    login_resp = sess.post(
        'https://www.esmplus.com/Member/SignIn/Authenticate',
        headers=headers, data=login_data)
    params = ( ('menuCode', 'TDM105'), )
    menu_resp = sess.get('https://www.esmplus.com/Escrow/Order/NewOrder',
        headers=headers, params=params)
    sel = Selector(text=menu_resp.text)
    return sel.xpath("//span[@id='divSellerAcc']//option[1]/@value")[0].extract()  # vulnerable


def get_search_condition(stage, start, end, searchKey, searchKeyword):
    if stage == 'neworder':
        return [('page', '1'),
                ('limit', '20'),
                ('siteGbn', '0'),
                ('searchDateType', 'ODD'),    # Ordered Day
                ('searchSDT', start),
                ('searchEDT', end),
                ('searchKey', searchKey),
                ('searchKeyword', searchKeyword),
                ('searchDistrType', 'AL'),
                ('searchAllYn', 'Y'),
                ('SortFeild', 'PayDate'),
                ('SortType', 'Desc'),
                ('start', '0'),
                ('searchTransPolicyType', ''),
               ]
    elif stage == 'todeliver':
        return [('page', '1'),
                ('limit', '100'),
                ('siteGbn', '0'),
                ('searchDateType', 'ODD'),
                ('searchSDT', start),
                ('searchEDT', end),
                ('searchKey', searchKey),
                ('searchKeyword', searchKeyword),
                ('excelInfo', ''),
                ('searchStatus', '0'),
                ('searchAllYn', 'Y'),
                ('SortFeild', 'PayDate'),
                ('SortType', 'Desc'),
                ('start', '0'),
                ('searchOrderType', ''),
                ('searchDeliveryType', ''),
                ('searchPaking', 'false'),
                ('searchDistrType', 'AL'),
                ('searchTransPolicyType', ''),
               ]
    elif stage == 'sending':
        return [('page', '1'),
                ('limit', '20'),
                ('siteGbn', '0'),
                ('searchDateType', 'ODD'),
                ('searchSDT', start),
                ('searchEDT', end),
                ('searchKey', searchKey),
                ('searchKeyword', searchKeyword),
                ('searchDistrType', 'AL'),
                ('searchType', '0'),
                ('excelInfo', 'undefined'),
                ('searchStatus', '0'),
                ('searchAllYn', 'N'),
                ('SortFeild', 'PayDate'),
                ('SortType', 'Desc'),
                ('start', '0'),
                ('searchTransPolicyType', ''),
               ]
    elif stage == "toreturn":
        return [('page', '1'),
                ('limit', '20'),
                ('siteGbn', '1'),
                ('searchDateType', ''),
                ('searchSDT', start),
                ('searchEDT', end),
                ('searchType', 'RR'),
                ('searchKey', searchKey),
                ('searchKeyword', searchKeyword),
                ('OrderByType', ''),
                ('excelInfo', ''),
                ('searchStatus', 'RR'),
                ('searchAllYn', 'N'),
                ('tabGbn', 1),
                ('SortFeild', 'PayDate'),
                ('SortType', 'Desc'),
                ('start', '0'),
                ('searchDistrType', 'AL'),
                ('searchRewardStatus', 'NN'),
                ('searchFastRefundYn', ''),
               ]
    elif stage == "toexchange":
        return [('page', '1'),
                ('limit', '100'),
                ('siteGbn', '1'),
                ('searchDateType', ''),
                ('searchSDT', start),
                ('searchEDT', end),
                ('searchType', ''),
                ('searchKey', searchKey),
                ('searchKeyword', searchKeyword),
                ('orderByType', ''),
                ('excelInfo', ''),
                ('searchStatus', 'EP'), # Somehow you get all types of entries with this
                ('searchAllYn', 'N'),
                ('tabGbn', '1'),
                ('SortFeild', 'PayDate'),
                ('SortType', 'Desc'),
                ('claimCount', '-'),
                ('start', '0'),
                ('searchDistrType', 'AL'),
               ]
    return None


search_urls = {
    'neworder': 'https://www.esmplus.com/Escrow/Order/NewOrderSearch',
    'todeliver': 'https://www.esmplus.com/Escrow/Delivery/GeneralDeliverySearch',
    'sending': 'https://www.esmplus.com/Escrow/Delivery/GetSendingSearch',
    'toreturn': 'https://www.esmplus.com/Escrow/Claim/ReturnManagementSearch',
    'toexchange': 'https://www.esmplus.com/Escrow/Claim/ExchangeManagementSearch',
}


def search(id, pw, stage, site, start, end,
                 searchKey, searchKeyword):
    # moved to the caller(in views.py)
    # start = str(start) if start else (timezone.now() -
    #       timezone.timedelta(days=30)).strftime("%Y-%m-%d")
    # end = str(end) if end else timezone.now().strftime("%Y-%m-%d")

    start = str(start)
    end = str(end)

    with requests.Session() as sess:
        mID = login(sess, id, pw, site)
        data = get_search_condition(
            stage, start, end, searchKey, searchKeyword)
        if stage in ("toreturn", "toexchange"):
            data.append( ('searchAccount', "TA^" + mID) )
        else:
            data.append( ('searchAccount', mID) )
        resp = sess.post(search_urls[stage],
                  headers=headers, data=data)
        return mID, json.loads(resp.text)


# confirm_urls = {
#     'neworder': 'https://www.esmplus.com/Escrow/Order/OrderCheck',
#     'todeliver': 'https://www.esmplus.com/Escrow/Delivery/SetDoShippingGeneral',
#     # 'sending': 'https://www.esmplus.com/Escrow/Delivery/GetSendingSearch',
#     # 'toreturn': 'https://www.esmplus.com/Escrow/Claim/ReturnManagementSearch',
#     # 'toexchange': 'https://www.esmplus.com/Escrow/Claim/ExchangeManagementSearch',
# }
#
# def confirm(id, pw, stage, order_info):
#     with requests.Session() as sess:
#         mID = login(sess, id, pw, site)
#         data = {
#             'mID': mID,
#             'orderInfo': order_info,
#         }
#         return sess.post(confirm_urls['stage'], data=data)

def neworder_confirm(id, pw, site, order_info):
    with requests.Session() as sess:
        mID = login(sess, id, pw, site)
        data = {
            "mID": mID,
            "orderInfo": order_info,
        }
        return sess.post("https://www.esmplus.com/Escrow/Order/OrderCheck",\
                         data=data)

def todeliver_confirm(id, pw, site, order_info):
    with requests.Session() as sess:
        mID = login(sess, id, pw, site)
        data = {
            "mID": mID,
            "deliveryInfo": order_info,
        }
        return sess.post("https://www.esmplus.com/Escrow/Delivery/SetDoShippingGeneral",\
                         data=data)

                                    # return_form_url ex) https://www.esmplus.com/
                                    # Escrow/Popup/ReturnProcess?oinf=2008278271,2,111421746,,
def toreturn_confirm(id, pw, site, return_form_url):
    with requests.Session() as sess:
        mID = login(sess, id, pw, site)
        form_resp = sess.get(return_form_url,
                             headers=headers)
        stream = io.StringIO(form_resp.text)
        form = parse(stream).getroot().xpath('//form')[0]
        form.action = 'https://www.esmplus.com/Escrow/Popup/SetReturnProcess'
        form.fields['PickupYN'] = 'Y'
        form.fields['RefundYN'] = 'Y'
        form.fields['RefundHoldYN'] = 'N'
        return sess.post(form.action, data=dict(form.fields))


def toexchange_confirm(id, pw, site, exchange_form_url,
                       comp, invoice):
    with requests.Session() as sess:
        mID = login(sess, id, pw, site)
        form_resp = sess.get(exchange_form_url,
                             headers=headers)
        stream = io.StringIO(form_resp.text)
        form = parse(stream).getroot().xpath('//form')[0]
        form.action = 'https://www.esmplus.com/Escrow/Popup/SetExchangeProcess'
        form.fields['PickupYN'] = 'Y'
        form.fields['ResendYN'] = 'Y'
        form.fields['resendCompCode'] = comp
        form.fields['resendInvoiceNo'] = invoice
        return sess.post(form.action, data=dict(form.fields))
