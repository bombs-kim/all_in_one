import json
import js2py
import requests
import sys
from datetime import datetime
from lxml.html import parse, submit_form

from lxml.html import parse, submit_form
from pprint import pprint
from scrapy.selector import Selector
from django.utils import timezone

# js2py.translate_file("storefarm_common_all.js", "storefarm_common_all_trans.py")
from .storefarm_common_all_trans import storefarm_common_all_trans as store_trans

headers = {
    'origin': 'https://nid.naver.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8,ko;q=0.6',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'cache-control': 'max-age=0',
    'authority': 'nid.naver.com',
    'referer': 'https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fsell.storefarm.naver.com%2F%23%2FnaverLoginCallback%3Furl%3Dhttps%253A%252F%252Fsell.storefarm.naver.com%252F%2523%252Fhome%252Fdashboard',
}

ID = 'bluewhale8202'
PW = 'k016317'

# Returns account number
def login(sess, id, pw):
    nhn_resp = sess.get(
        'https://nid.naver.com/login/ext/keys_js2.nhn', headers=headers)
    parts = nhn_resp.text.split(";")
    parts = [ parts[i].split("'")[1] for i in range(4)]
    sessionkey, keyname, evalue, nvalue = parts[0], parts[1], parts[2], parts[3]
    # Too much computation time spent here
    # Possibly needed to be replaced with a faster method
    encpw = store_trans.get_encpw(sessionkey, evalue, nvalue, id, pw)

    data = [
      ('enctp', '1'),       ('encpw', encpw),
      ('encnm', keyname),   ('svctype', '0'),
      ('svc', ''),          ('viewtype', '0'),
      ('locale', 'en_US'),  ('postDataKey', ''),
      ('smart_LEVEL', '1'), ('logintp', ''),
      ('url', 'https://sell.storefarm.naver.com/#/naverLoginCallback'
              '?url=https%3A%2F%2Fsell.storefarm.naver.com%2F%23%2Fhome%2Fdashboard'),
      ('localechange', ''), ('theme_mode', ''),
      ('ls', ''),           ('pre_id', ''),
      ('resp', ''),         ('exp', ''),
      ('ru', ''), ('id', ''), ('pw', ''),
    ]
    # get NID_AUTH cookie
    sess.post('https://nid.naver.com/nidlogin.login',
              headers=headers, data=data)
    # get NSI cookie
    sess.get('https://sell.storefarm.naver.com/api/login/init', headers=headers)

"""
Naver Storefarm json response structure
{'bSuccess': True,
 'htReturnValue': {'pagedResult': {'aggregated': False,
                                   'content': [...],
                                   'number': 2, // page number
                                   'size': 100, // page size
                                   'total': 1072 // total entries
                                   }}}
"""

# 전체 stages
# 발주/발송 관리
#  -'NEW_ORDER': 신규주문 => neworder
#  -'PLACE_ORDER': 발주확인 => deliver
#  -'PLACE_ORDER_RELEASE': 발주확인해제 ! 얘가 문제 => deliver_release
# 배송중 delivering
# 취소 cancel
# 반품 refund
# 교환 exchange

# # ('ON', '주문번호'), # Only supported for global search
# ('GN', '상품번호'),
# #('GM', '상품명'), # Not supported for storefarm
# ('BN', '구매자이름'),
# ('BI', '구매자ID'),
# #('RCV', '수령인명') # Not supported for neworder stage

get_storefarm_search_type_from_key = {
    'ON': 'PRODUCT_ORDER_NO',
    'GN': 'PRODUCT_NO',
    'BN': 'PURCHASER_NAME',
    'BI': 'PURCHASER_ID',
    '': '',
    }

get_storefarm_status_from_stage = {
    'neworder': 'NEW_ORDER',
    'deliver': 'PLACE_ORDER',
    'deliver_release': 'PLACE_ORDER_RELEASE',
}

def get_search_condition1(stage, start, end, searchKey, searchKeyword):
    search_type = get_storefarm_search_type_from_key[searchKey]
    # An empty search string is not allowed for any specific search_type.
    # If you don't want to search on a string, search_type shouldn't be
    # specified (i.e. search_type should be empty string)
    if searchKeyword == '':
        search_type = ''
                # These three stages share the same form
    if stage in ('neworder', 'deliver', 'deliver_release'):
        data = [
          ('orderStatus', 'WAITING_DISPATCH'),
          ('detailedOrderStatus', get_storefarm_status_from_stage[stage]),
          ('deliveryMethodType', ''),
          ('deviceClassType', ''),
          ('delayDispatchGuideTreatStateType', ''),
          ('detailSearch.type', search_type),
          ('detailSearch.keyword', searchKeyword),
          ('dateRange.type', 'PAY_COMPLETED'),
          ('dateRange.fromDate', start),
          ('dateRange.toDate', end),
          ('paging.current', '1'),
          ('rowPerPageType', 'ROW_CNT_500'),
          ('sort.type', 'RECENTLY_ORDER_YMDT'),
          ('sort.direction', 'DESC'),
          ('onlyValidation', 'true'),
        ]
    elif stage == "deliverstatus":
        data = [
          ('orderStatus', 'ALL'),
          ('detailedOrderStatus', 'ALL'),
          ('purchaseDecisionRequestYn', ''),
          ('detailSearch.type', search_type),
          ('detailSearch.keyword', searchKeyword),
          ('dateRange.type', 'PAY_COMPLETED'),
          ('dateRange.fromDate', start),
          ('dateRange.toDate', end),
          ('paging.current', '1'),
          ('rowPerPageType', 'ROW_CNT_500'),
          ('sort.direction', 'DESC'),
          ('onlyValidation', 'true'),
        ]

    # override some fields
    if search_type == "PRODUCT_ORDER_NO":
        pass

    return data

# For now searchtype and searchkey is not used
def get_search_condition2(stage, status, start, end):
    status_field =  'claimStatus' if stage == 'exchange'\
                    else 'productOrder.lastClaim.claimStatus'
    types = {
        'cancel': 'CLAIM_REQUEST',
        'refund': 'RETURN_REQUEST',
        'exchange': 'EXCHANGE_REQUEST'}

    params = (('range.type', types[stage]),
        ('range.fromDate', start),
        ('range.toDate', end),
        (status_field, status),
        ('detailSearch.type', ''),
        # ('detailSearch.keyword', searchKeyword),
        ('paging.current', '1'),
        ('paging.rowsPerPage', '500'),
    )
    return params


search_urls = {
    'neworder': 'https://sell.storefarm.naver.com/o/n/sale/delivery/json',
    'deliver': 'https://sell.storefarm.naver.com/o/n/sale/delivery/json',
    'deliverstatus': 'https://sell.storefarm.naver.com/o/n/sale/delivery/situation/json',
    'cancel': 'https://sell.storefarm.naver.com/o/claim/cancel/json',
    'refund': 'https://sell.storefarm.naver.com/o/claim/return/json',
    'exchange': 'https://sell.storefarm.naver.com/o/claim/exchange/json',
}

# Used for confirming
def attach_order_info(entries, account, stage):
    # SiteIDValue and SiteIdValue are two different keys
    for entry in entries:
        order_info = '/'.join(str(val) for val in
                              [account.site, account.userid, entry['PRODUCT_ORDER_ID']]  )
        # if stage == 'neworder':
        #     order_info += ',' + ','.join(str(entry[key]) for key in
        #         ('SiteIDValue', 'SellerCustNo') )
        # elif stage == 'cancel':
        #     order_info += ',' + ','.join(str(entry[key]) for key in
        #         ('SiteIdValue', 'SellerCustNo', 'ClaimReasonCode') )
        # elif stage == 'exchange':
        #     order_info += ',' + ','.join(str(entry[key]) for key in
        #         ('SiteIdValue', 'SellerCustNo') )
        # elif stage == 'refund':
        #     order_info += ',' + ','.join(str(entry[key]) for key in
        #         ('SiteIdValue', 'SellerCustNo', 'ReturnInvoiceNo') )
        #     delivery_comp = str(
        #         entry['ReturnDeliveryComp']
        #         ) if entry['ReturnDeliveryComp'] else ''
        #     order_info += ',' + delivery_comp
        entry['orderInfo__'] = order_info

def search(account, stage, start, end,
                 searchKey, searchKeyword):
    start = start.strftime("%Y.%m.%d")
    end = end.strftime("%Y.%m.%d")

    with requests.Session() as sess:
        login(sess, account.userid, account.password)
        entries = []
        if stage in ('cancel', 'refund', 'exchange'):
            # Could be improved with grequests(asynchronous)
            statuses = {
                'cancel': ('CANCEL_REQUEST', 'CANCELING',),
                        #    'CANCEL_DONE', 'CANCEL_REJECT'),
                'refund': ('RETURN_REQUEST', 'COLLECTING', 'COLLECT_DONE'),
                # ('RETURN_DONE', 'RETURN_REJECT'):
                'exchange': ('EXCHANGE_REQUEST', 'COLLECTING',
                               'COLLECT_DONE', 'EXCHANGE_REDELIVERING',
                               'EXCHANGE_DONE', 'EXCHANGE_REJECT',)}
            for status in statuses[stage]:
                params = get_search_condition2(stage, status, start, end)
                resp = sess.get(search_urls[stage],
                          headers=headers, params=params)
                cur_entries = json.loads(resp.text)\
                                ["htReturnValue"]["pagedResult"]["content"]
                for entry in cur_entries:
                    entry["status"] = status
                entries += cur_entries

        else:
            data = get_search_condition1(
                stage, start, end, searchKey, searchKeyword)
            resp = sess.post(search_urls[stage],
                      headers=headers, data=data)
            entries = json.loads(resp.text)["htReturnValue"]["pagedResult"]["content"]
        attach_order_info(entries, account, stage)
        return entries



def neworder_confirm(id, pw, site, order_info):
    with requests.Session() as sess:
        login(sess, id, pw)
        headers = {
            'origin': 'https://sell.storefarm.naver.com',
            # 'accept-encoding': 'gzip, deflate, br',
            'x-requested-with': 'XMLHttpRequest',
            'accept-language': 'en-US,en;q=0.8,ko;q=0.6',
            # 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'accept': '*/*',
            'charset': 'utf-8',
            'referer': 'https://sell.storefarm.naver.com/o/n/sale/delivery', ###
            'authority': 'sell.storefarm.naver.com',
        }
        data = [    # order_info ex) '2017091223865501,2017091223863221,2017091223860081'
          ('productOrderIds', order_info),
          ('path', 'placeOrder'),
          ('onlyValidation', 'true'),
          ('validationSuccess', 'true'),
        ]
        resp = sess.post('https://sell.storefarm.naver.com/o/sale/delivery/placeOrder',
                  headers=headers, data=data)
        return j['htReturnValue']['results']


def deliver_confirm(id, pw, orders):
    with requests.Session() as sess:
        login(sess, id, pw)
        headers = {
            'origin': 'https://sell.storefarm.naver.com',
            # 'accept-encoding': 'gzip, deflate, br',
            'x-requested-with': 'XMLHttpRequest',
            'accept-language': 'en-US,en;q=0.8,ko;q=0.6',
            # 'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            # 'accept': '*/*',
            'charset': 'utf-8',
            'referer': 'https://sell.storefarm.naver.com/o/n/sale/delivery',
            'authority': 'sell.storefarm.naver.com',
        }
        today = datetime.now().strftime("%Y.%m.%d")
        data = [('checkValidation', 'true'), ('validationSuccess', 'true')]
        for idx, (product_id, company, invoice) in enumerate(orders):
            data += [
                ('dispatchForms[%d].productOrderId' % idx, product_id),
                ('dispatchForms[%d].deliveryMethodType' % idx, 'DELIVERY'),
                ('dispatchForms[%d].searchOrderStatusType' % idx, 'WAITING_DISPATCH'),
                ('dispatchForms[%d].deliveryCompanyCode' % idx, company),
                ('dispatchForms[%d].invoicingNo' % idx, invoice),
                ('dispatchForms[%d].dispatchYmdt' % idx, today),  # Not sure. need to be checked
            ]

        resp = sess.post('https://sell.storefarm.naver.com/o/sale/delivery/dispatch2',
                             headers=headers, data=data)
        return resp


def cancel_confirm(id, pw, order_info):
    with requests.Session() as sess:
        login(sess, id, pw)
        headers = {
            'origin': 'https://sell.storefarm.naver.com',
            'x-requested-with': 'XMLHttpRequest',
            'accept-language': 'en-US,en;q=0.8,ko;q=0.6',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'charset': 'utf-8',
            'referer': 'https://sell.storefarm.naver.com/o/claim/cancel',
            'authority': 'sell.storefarm.naver.com',
        }
        data = [    # order_info ex) '2017091223865501,2017091223863221,2017091223860081'
          ('productOrderIds', order_info),
          ('onlyValidation', 'true'),
          ('validationSuccess', 'true'),
        ]
        resp = sess.post('https://sell.storefarm.naver.com/o/claim/cancel/operation/' +
                         order_info +'/refund',
                  headers=headers, data=data)
        return resp


def cancel_deliver(account, product_order_id, company, invoice):
    with requests.Session() as sess:
        login(sess, account.userid, account.password)
        headers = {
            'accept-language': 'en-US,en;q=0.8,ko;q=0.6',
            'upgrade-insecure-requests': '1',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'cache-control': 'max-age=0',
            'authority': 'sell.storefarm.naver.com',
            'referer': 'https://sell.storefarm.naver.com/o/claim/cancel',
        }
        form_url = ('https://sell.storefarm.naver.com/o/claim/cancel/dispatch/' +
                   product_order_id + '/request')
        # Response form will be used to authenticate and process return
        form_resp = sess.get(form_url,
                             headers=headers)
        stream = io.StringIO(form_resp.text)
        form = parse(stream).getroot().xpath('//form')[0]
        form.fields['cancelDispathArray[0].serviceCompanyCode'] = company
        form.fields['cancelDispathArray[0].invoiceNo'] = invoice
        form.fields['cancelDispathArray[0].deliveryMethod'] = 'DELIVERY'
        today = datetime.now().strftime("%Y.%m.%d")
        form.fields['cancelDispathArray[0].deliveryYmdt'] = today
        # form.fields['onlyValidation'] = 'true'   # necessary?
        url_base = 'https://sell.storefarm.naver.com'
        resp = sess.post(url_base + form.action, data=dict(form.fields))

        return resp
#
# def neworder_confirm(id, pw, site, order_info):
#     with requests.Session() as sess:
#         mID = login(sess, id, pw, site)
#         data = {
#             "mID": mID,
#             "orderInfo": order_info,
#         }
#         return sess.post("https://www.esmplus.com/Escrow/Order/OrderCheck",\
#                          data=data)
#
#                                     # return_form_url ex) https://www.esmplus.com/
#                                     # Escrow/Popup/ReturnProcess?oinf=2008278271,2,111421746,,
# def toreturn_confirm(id, pw, site, return_form_url):
#     with requests.Session() as sess:
#         mID = login(sess, id, pw, site)
#         form_resp = sess.get(return_form_url,
#                              headers=headers)
#         stream = io.StringIO(form_resp.text)
#         form = parse(stream).getroot().xpath('//form')[0]
#         form.action = 'https://www.esmplus.com/Escrow/Popup/SetReturnProcess'
#         form.fields['PickupYN'] = 'Y'
#         form.fields['RefundYN'] = 'Y'
#         form.fields['RefundHoldYN'] = 'N'
#         return sess.post(form.action, data=dict(form.fields))



#
# # 발주/발송관리
# 'https://sell.storefarm.naver.com/o/n/sale/delivery/json'
# """
# 'NEW_ORDERS'
# 'NEW_ORDERS_DELAYED'
# 'DELIVERY_READY'
# 'DELIVERY_READY_DELAYED'
# """
#
# # 배송현황 관리
# 'https://sell.storefarm.naver.com/o/n/sale/delivery/situation/json'
# """
# 'DELIVERING'
# 'DELIVERED'
# 'MATTER_ON_DELIVERY' (배송중 문제)
# 'NORMAL_PURCHASE_DECISION_EXTENSION' (구매확정연장)
# 'PURCHASE_DECISION_HOLDBACK_ACCEPT' (구매확정보류 접수)
# 'PURCHASE_DECISION_HOLDBACK_REDELIVERING' (구매확정보류 재배송중)
# 'PURCHASE_DECISION_REQUEST' (구매확정요청)
# """
#
# # 구매확정 내역
# 'https://sell.storefarm.naver.com/o/sale/purchaseDecision/json'
# 'PURCHASE_DECIDED'
#
# # 취소관리
# 'https://sell.storefarm.naver.com/o/claim/cancel/json?summaryInfoType=CANCEL_REQUEST'
# cancel_summaryInfoType = ('CANCEL_REQUEST', 'CANCEL_DELAYED',
#                           'CANCEL_DONE')
#
# # 반품 관리
# 'https://sell.storefarm.naver.com/o/claim/return/json?summaryInfoType=RETURN_REQUEST'
# return_summaryInfoType = ('RETURN_REQUEST', 'RETURN_COLLECTING',
#                    'RETURN_COLLECT_DONE', 'RETURN_HOLDBACK',
#                    'RETURN_DELAYED', 'RETURN_AUTO_WAITING_REFUND')
#
# # 교환 관리
# 'https://sell.storefarm.naver.com/o/claim/exchange/json?summaryInfoType=EXCHANGE_REQUEST'
# exchange_summaryInfoType = ('EXCHANGE_REQUEST','EXCHANGE_COLLECTING',
#                    'EXCHANGE_COLLECT_DONE', 'EXCHANGE_HOLDBACK',
#                    'EXCHANGE_DELAYED', 'EXCHANGE_PURCHASE_DECISION_EXTENSION')
