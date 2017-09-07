import io
import json
import js2py
import requests
import sys
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
#  -'PLACE_ORDER': 발주확인 => todeliver
#  -'PLACE_ORDER_RELEASE': 발주확인해제 ! 얘가 문제 => todeliver_release
# 배송중 delivering
# 취소 cancel
# 반품 toreturn
# 교환 toexchange

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
    'todeliver': 'PLACE_ORDER',
    'todeliver_release': 'PLACE_ORDER_RELEASE',
}

def get_search_condition1(stage, start, end, searchKey, searchKeyword):
    search_type = get_storefarm_search_type_from_key[searchKey]
    # An empty search string is not allowed for any specific search_type.
    # If you don't want to search on a string, search_type shouldn't be
    # specified (i.e. search_type should be empty string)
    if searchKeyword == '':
        search_type = ''
                # These three stages share the same form
    if stage in ('neworder', 'todeliver', 'todeliver_release'):
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
    elif stage == "sending":
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
def get_search_condition2(type, status, start, end):
    status_field = 'productOrder.lastClaim.claimStatus' if type == 'toreturn'\
                    else 'claimStatus'
    params = (('range.type', type),
        ('range.fromDate', start),
        ('range.toDate', end),
        (status_field, status),
        ('detailSearch.type', ''),
        # ('detailSearch.keyword', searchKeyword),
        ('paging.current', '1'),
        ('paging.rowsPerPage', '500'),
    )
    return params


# sess = requests.session()
# login(sess,ID,PW)
# resp = sess.post('https://sell.storefarm.naver.com/o/n/sale/delivery/json', headers=headers, data=data)
# j = json.loads(resp.text)

search_urls = {
    'neworder': 'https://sell.storefarm.naver.com/o/n/sale/delivery/json',
    'todeliver': 'https://sell.storefarm.naver.com/o/n/sale/delivery/json',
    'sending': 'https://sell.storefarm.naver.com/o/n/sale/delivery/situation/json',
    'toreturn': 'https://sell.storefarm.naver.com/o/claim/return/json',
    'toexchange': 'https://sell.storefarm.naver.com/o/claim/exchange/json',
}


def search(id, pw, stage, site, start, end,
                 searchKey, searchKeyword):
    start = start.strftime("%Y.%m.%d")
    end = end.strftime("%Y.%m.%d")

    with requests.Session() as sess:
        login(sess, id, pw)
        entries = []
        if stage  == 'toreturn' or stage == 'toexchange':
            # Could be improved with grequests(asynchronous)
            statuses = {
                # 'RETURN_DONE', 'RETURN_REJECT'):
                'toreturn': ('RETURN_REQUEST', 'COLLECTING', 'COLLECT_DONE'),
                'toexchange': ('EXCHANGE_REQUEST', 'COLLECTING',
                               'COLLECT_DONE', 'EXCHANGE_REDELIVERING',
                               'EXCHANGE_DONE', 'EXCHANGE_REJECT',)}
            type = 'RETURN_REQUEST' if stage == 'toreturn' else 'EXCHANGE_REQUEST'
            for status in statuses[stage]:
                params = get_search_condition2(type, status, start, end)
                resp = sess.get(search_urls[stage],
                          headers=headers, params=params)
                cur_entries = json.loads(resp.text)\
                                ["htReturnValue"]["pagedResult"]["content"]
                for entry in cur_entries:
                    entry["status"] = status
                entries += cur_entries
            return entries

        else:
            data = get_search_condition1(
                stage, start, end, searchKey, searchKeyword)
            resp = sess.post(search_urls[stage],
                      headers=headers, data=data)
            return json.loads(resp.text)["htReturnValue"]["pagedResult"]["content"]
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
