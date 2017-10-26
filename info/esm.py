import io
import json
import requests
import sys
from lxml.html import parse, submit_form
from pprint import pprint
from scrapy import Selector
from datetime import datetime
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
    'Connection': 'keep-alive',
}

# Set login cookie for the session received and
# returns mID, which will be used for subsequent tasks
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
    # vulnerable
    return sel.xpath("//span[@id='divSellerAcc']//option[1]/@value")[0].extract()


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
    elif stage == 'deliver':
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
    elif stage == 'deliverstatus':
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
    elif stage == "cancel":
        return  [('page', '1'),
                 ('limit', '20'),
                 ('siteGbn', '1'),
                 ('searchAccount', 'TA'),  # ??
                 ('searchDateType', 'ODD'),
                 ('searchSDT', start),
                 ('searchEDT', end),
                 ('searchType', 'CR'),
                 ('searchKey', searchKey),
                 ('searchKeyword', searchKeyword),
                 ('orderByType', ''),
                 ('excelInfo', ''),
                 ('searchStatus', 'CR'),  # search requested?
                 ('searchAllYn', 'N'),
                 ('tabGbn', '1'),
                 ('SortFeild', 'PayDate'),
                 ('SortType', 'Desc'),
                 ('start', '0'),
                 ('searchDistrType', 'AL'),
                ]
    elif stage == "refund":
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
    elif stage == "exchange":
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
    'deliver': 'https://www.esmplus.com/Escrow/Delivery/GeneralDeliverySearch',
    'deliverstatus': 'https://www.esmplus.com/Escrow/Delivery/GetSendingSearch',
    'cancel': 'https://www.esmplus.com/Escrow/Claim/CancelManagementSearch',
    'refund': 'https://www.esmplus.com/Escrow/Claim/ReturnManagementSearch',
    'exchange': 'https://www.esmplus.com/Escrow/Claim/ExchangeManagementSearch',
}


# Attach an attribut named orderInfo to entries.
# orderInfo will be used for confirming
def attach_order_info(entries, account, stage):
    # Warning: SiteIDValue and SiteIdValue are two different keys
    for entry in entries:
        order_info = '/'.join(str(val) for val in
                              [account.site, account.userid, entry['OrderNo']]  )
        if stage == 'neworder':
            order_info += ',' + ','.join(str(entry[key]) for key in
                ('SiteIDValue', 'SellerCustNo') )
        elif stage == 'cancel':
            order_info += ',' + ','.join(str(entry[key]) for key in
                ('SiteIdValue', 'SellerCustNo', 'ClaimReasonCode') )
        elif stage == 'exchange':
            order_info += ',' + ','.join(str(entry[key]) for key in
                ('SiteIdValue', 'SellerCustNo') )
        elif stage == 'refund':
            order_info += ',' + ','.join(str(entry[key]) for key in
                ('SiteIdValue', 'SellerCustNo', 'ReturnInvoiceNo') )
            delivery_comp = str(
                entry['ReturnDeliveryComp']
                ) if entry['ReturnDeliveryComp'] else ''
            order_info += ',' + delivery_comp
        entry['orderInfo__'] = order_info


def search(account, stage, start, end,
                 searchKey, searchKeyword):
    global headers
    _headers = headers

    start = str(start)
    end = str(end)

    with requests.Session() as sess:
        mID = login(sess, account.userid, account.password, account.site)
        data = get_search_condition(
            stage, start, end, searchKey, searchKeyword)
        if stage in ('refund', 'exchange'):
            data.append( ('searchAccount', "TA^" + mID) )
        elif stage == 'cancel':
            _headers = dict(_headers)
            _headers["Referer"] = 'https://www.esmplus.com/Escrow/Claim/CancelRequestManagement?menuCode=TDM115'
        else:
            data.append( ('searchAccount', mID) )
        resp = sess.post(search_urls[stage],
                  headers=_headers, data=data)
    entries = json.loads(resp.text)['data']
    attach_order_info(entries, account, stage)
    return entries


# Attach local datetime that would be used as the sorting criteria
def attach_local_datetime(entries, tz):
    for entry in entries:
        dt = datetime.strptime(
            entry['DepositConfirmDate'], "%Y-%m-%d %H:%M:%S")
        entry['datetime__'] = tz.localize(dt)

################################  To do  #######################################
# Input and return types of the follwoing functions(ex. neworder_confirm)
# are not consistent. Need to be refactored to receive only account(not id, pw)
# and to have one return type, say, pased JSON data


def neworder_confirm(id, pw, site, order_info):
    with requests.Session() as sess:
        mID = login(sess, id, pw, site)
        data = {
            "mID": mID,
            "orderInfo": order_info,
        }
        return sess.post("https://www.esmplus.com/Escrow/Order/OrderCheck",\
                         data=data)


def deliver_confirm(id, pw, site, order_info):
    with requests.Session() as sess:
        mID = login(sess, id, pw, site)
        data = {
            "mID": mID,
            "deliveryInfo": order_info,
        }
        return sess.post("https://www.esmplus.com/Escrow/Delivery/SetDoShippingGeneral",\
                         data=data)


def cancel_confirm(account, order_info):
    with requests.Session() as sess:
        login(sess, account.userid, account.password, account.site)
        query = "?orderInfos=" + order_info
        resp = sess.get("https://www.esmplus.com/Escrow/Popup/CancelRequestConfirmCancel"
                        + query)
        sel = Selector(text=resp.text)
        return "\n".join(sel.xpath("//tbody//td//text()").extract())


def cancel_deliver(account, order_info, comp, comp_name, inv):
    with requests.Session() as sess:
        login(sess, account.userid, account.password, account.site)
        query = "?deliveryInfos=" + ",".join([order_info, comp, comp_name, inv])
        resp = sess.get("http://www.esmplus.com/Escrow/Popup/CancelRequestShipping"
                        + query)
        sel = Selector(text=resp.text)
        # ex) "\n".join(['실패', 'G마켓', '2564302794', '1110120028', '게임악세사리',
        #        '발송처리 실패 [A : G001,송장 번호 길이가 맞지 않습니다.]', '\xa0'])
        return "\n".join(sel.xpath("//tbody//td//text()").extract())


###############################  Note  #########################################
# Confirming refund and exchange is not an simple task. A user of esmplus is
# supposed to open up a new dialog window to proceed to begin with. I mimiced
# this process by parsing the response without resorting to web browsers.
# Becaused the dialog response is complicated it's almost infeasible to
# parse it manually. So I parsed the dialog with lxml.html.parse function
# and made subsequent requests to actually confirm a refund or exchange.

#  order_info format
# OrderNo,SiteIdValue,SellerCustNo,returnInvoiceNo,returnDeliveryComp
# ex) 2008278271,2,111421746,,


def refund_confirm(id, pw, site, order_info):
    """  order_info format
       OrderNo,SiteIdValue,SellerCustNo,returnInvoiceNo,returnDeliveryComp
       ex) 2008278271,2,111421746,,
    """
    with requests.Session() as sess:
        mID = login(sess, id, pw, site)
        form_url = 'https://www.esmplus.com/Escrow/Popup/ReturnProcess'
        form_url += "?oinf=" + order_info
        form_resp = sess.get(form_url,
                             headers=headers)
        stream = io.StringIO(form_resp.text)
        form = parse(stream).getroot().xpath('//form')[0]
        form.action = 'https://www.esmplus.com/Escrow/Popup/SetReturnProcess'
        form.fields['PickupYN'] = 'Y'
        form.fields['RefundYN'] = 'Y'
        form.fields['RefundHoldYN'] = 'N'
        resp = sess.post(form.action, data=dict(form.fields))
        return json.loads(resp.text)


def exchange_confirm(id, pw, site, order_info,
                       comp, invoice):
    """ order_info format
      OrderNo,SiteIdValue,SellerCustNo
      2008278271,2,111421746
    """
    with requests.Session() as sess:
        mID = login(sess, id, pw, site)
        form_url = 'https://www.esmplus.com/Escrow/Popup/ExchangeProcess'
        form_url += "?oinf=" + order_info
        pprint(form_url)
        form_resp = sess.get(form_url,
                             headers=headers)
        stream = io.StringIO(form_resp.text)
        form = parse(stream).getroot().xpath('//form')[0]
        form.action = 'https://www.esmplus.com/Escrow/Popup/SetExchangeProcess'
        form.fields['PickupYN'] = 'Y'
        form.fields['ResendYN'] = 'Y'
        form.fields['resendCompCode'] = comp
        form.fields['resendInvoiceNo'] = invoice
        resp = sess.post(form.action, data=dict(form.fields))
        return json.loads(resp.text)
