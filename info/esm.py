import requests
import json
import sys
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
                ('limit', '100'),
                ('siteGbn', '1'),
                # ('searchAccount', 'TA^341270'),
                ('searchDateType', 'ODD'),
                ('searchSDT', start),
                ('searchEDT', end),
                ('searchType', 'PR'),
                ('searchKey', searchKey),
                ('searchKeyword', searchKeyword),
                ('OrderByType', ''),
                ('excelInfo', ''),
                ('searchStatus', 'PR'),
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
                ('searchStatus', ''),
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
                 searchKey='ON', searchKeyword=''):
    start = str(start) if start else (timezone.now() -
          timezone.timedelta(days=30)).strftime("%Y-%m-%d")
    end = str(end) if end else timezone.now().strftime("%Y-%m-%d")

    with requests.Session() as sess:
        mID = login(sess, id, pw, site)
        data = get_search_condition(stage, start, end, searchKey, searchKeyword)
        if stage in ("toreturn", "toexchange"):
            data.append( ('searchAccount', "TA^" + mID) )
        else:
            data.append( ('searchAccount', mID) )
        resp = sess.post(search_urls[stage],
                  headers=headers, data=data)
        return mID, json.loads(resp.text)


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


#
#
# def get_neworder(id, pw, site, start=None, end=None,
#                  searchKey='ON', searchKeyword=''):
#     start = str(start) if start else (timezone.now() -
#           timezone.timedelta(days=30)).strftime("%Y-%m-%d")
#     end = str(end) if end else timezone.now().strftime("%Y-%m-%d")
#
#     with requests.Session() as sess:
#         mID = login(sess, id, pw, site)
#         neworder_data = [
#           ('page', '1'),
#           ('limit', '20'),
#           ('siteGbn', '0'),
#           # ('searchAccount', '341270'),
#           ('searchDateType', 'ODD'),    # Ordered Day
#           ('searchSDT', start),
#           ('searchEDT', end),
#           ('searchKey', searchKey),
#           ('searchKeyword', searchKeyword),
#           ('searchDistrType', 'AL'),
#           ('searchAllYn', 'Y'),
#           ('SortFeild', 'PayDate'),
#           ('SortType', 'Desc'),
#           ('start', '0'),
#           ('searchTransPolicyType', ''),
#         ]
#         neworder_data.append( ('searchAccount', mID) )
#         neworder_resp = sess.post('https://www.esmplus.com/Escrow/Order/NewOrderSearch',
#                   headers=headers, data=neworder_data)
#
#         return mID, json.loads(neworder_resp.text)
#
# # 발송대기
# def get_todeliver(id, pw, site, start=None, end=None,
#                  searchKey='ON', searchKeyword=''):
#     start = str(start) if start else (timezone.now() -
#           timezone.timedelta(days=30)).strftime("%Y-%m-%d")
#     end = str(end) if end else timezone.now().strftime("%Y-%m-%d")
#
#     with requests.Session() as sess:
#         mID = login(sess, id, pw, site)
#         todeliver_data = [
#           ('page', '1'),
#           ('limit', '100'),
#           ('siteGbn', '0'),
#           # ('searchAccount', '341270'),
#           ('searchDateType', 'ODD'),
#           ('searchSDT', start),
#           ('searchEDT', end),
#           ('searchKey', searchKey),
#           ('searchKeyword', searchKeyword),
#           ('excelInfo', ''),
#           ('searchStatus', '0'),
#           ('searchAllYn', 'Y'),
#           ('SortFeild', 'PayDate'),
#           ('SortType', 'Desc'),
#           ('start', '0'),
#           ('searchOrderType', ''),
#           ('searchDeliveryType', ''),
#           ('searchPaking', 'false'),
#           ('searchDistrType', 'AL'),
#           ('searchTransPolicyType', ''),
#         ]
#         todeliver_data.append( ('searchAccount', mID) )
#         todeliver_resp = sess.post('https://www.esmplus.com/Escrow/Delivery/GeneralDeliverySearch',
#                       headers=headers, data=todeliver_data)
#
#         return mID, json.loads(todeliver_resp.text)
#
#
# # 배송중
# def get_sending(id, pw, site, start=None, end=None,
#                  searchKey='ON', searchKeyword=''):
#     start = str(start) if start else (timezone.now() -
#           timezone.timedelta(days=30)).strftime("%Y-%m-%d")
#     end = str(end) if end else timezone.now().strftime("%Y-%m-%d")
#
#     with requests.Session() as sess:
#         mID = login(sess, id, pw, site)
#         data = [
#           ('page', '1'),
#           ('limit', '20'),
#           ('siteGbn', '0'),
#           # ('searchAccount', '341270'),
#           ('searchDateType', 'ODD'),
#           ('searchSDT', start),
#           ('searchEDT', end),
#           ('searchKey', searchKey),
#           ('searchKeyword', searchKeyword),
#           ('searchDistrType', 'AL'),
#           ('searchType', '0'),
#           ('excelInfo', 'undefined'),
#           ('searchStatus', '0'),
#           ('searchAllYn', 'N'),
#           ('SortFeild', 'PayDate'),
#           ('SortType', 'Desc'),
#           ('start', '0'),
#           ('searchTransPolicyType', ''),
#         ]
#         data.append( ('searchAccount', mID) )
#         sending_resp = sess.post('https://www.esmplus.com/Escrow/Delivery/GetSendingSearch',
#                   headers=headers, data=data)
#         return mID, json.loads(sending_resp.text)
