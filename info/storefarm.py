import json
import js2py
import requests
import sys
from datetime import datetime
from lxml.html import parse, submit_form
from pprint import pprint
from scrapy.selector import Selector
from django.utils import timezone

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


# There are two login functions to be used for seller ID login and naver ID login.

# Naver ID login
def login_normal(sess, account):
    headers = {
        'pragma': 'no-cache',
        'origin': 'https://sell.storefarm.naver.com',
        'accept-encoding': 'gzip, deflate, br',
        'x-current-state': 'https://sell.storefarm.naver.com/#/login?url=https:~2F~2Fsell.storefarm.naver.com~2F%23~2Fhome~2Fdashboard',
        'accept-language': 'en-US,en;q=0.8,ko;q=0.6',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'accept': '*/*',
        'cache-control': 'no-cache',
        'authority': 'sell.storefarm.naver.com',
        'referer': 'https://sell.storefarm.naver.com/',
    }
    params = (
        ('url', 'https%3A%2F%2Fsell.storefarm.naver.com%2F%23%2Fhome%2Fdashboard'),
    )
    data = {
        'id': account.userid,
        'pw': account.password,
        'url': "https%3A%2F%2Fsell.storefarm.naver.com%2F%23%2Fhome%2Fdashboard",
    }
    resp = sess.post('https://sell.storefarm.naver.com/api/login',
        headers=headers, params=params, data=json.dumps(data))


# Sellor ID login.
# Naver tries to encrypt login credentials with a weird RSA algorithm, which
# adds no security to the login process. Encryption details can be found
# in the storefarm_common_all.js in the directory where this file is located.
# I commented out unused parts. storefarm_common_all_trans is a module that was
# translated from storefar_common_all.js.

def login_nid(sess, account):
    nhn_resp = sess.get(
        'https://nid.naver.com/login/ext/keys_js2.nhn', headers=headers)
    parts = nhn_resp.text.split(";")
    parts = [ parts[i].split("'")[1] for i in range(4)]
    sessionkey, keyname, evalue, nvalue = parts[0], parts[1], parts[2], parts[3]
    # Too much computation time spent here
    # Possibly needed to be replaced with a faster method
    encpw = store_trans.get_encpw(sessionkey, evalue, nvalue,
                                  account.userid, account.password)
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


def login(sess, account):
    if account.site == "STOREFARM":
        login_normal(sess, account)
    else:
        login_nid(sess, account)

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
        if stage in ('refund', 'exchange'):
            order_info += ',' + entry['ORDER_ID']
        entry['orderInfo__'] = order_info

def search(account, stage, start, end,
                 searchKey, searchKeyword):
    start = start.strftime("%Y.%m.%d")
    end = end.strftime("%Y.%m.%d")

    with requests.Session() as sess:
        login(sess, account)
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



def neworder_confirm(account, order_info):
    with requests.Session() as sess:
        login(sess, account)
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
        return resp


def deliver_confirm(account, orders):
    with requests.Session() as sess:
        login(sess, account)
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


def cancel_confirm(account, order_info):
    with requests.Session() as sess:
        login(sess, account)
        headers = {
            'origin': 'https://sell.storefarm.naver.com',
            'x-requested-with': 'XMLHttpRequest',
            'accept-language': 'en-US,en;q=0.8,ko;q=0.6',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'charset': 'utf-8',
            'referer': 'https://sell.storefarm.naver.com/o/claim/cancel',
            'authority': 'sell.storefarm.naver.com',
        }
        data = [
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
        login(sess, account)
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


def refund_collect_done(account, order_info):
    with requests.Session() as sess:
        login(sess, account)
        product_order_id, order_id = order_info.split(',')
        data = [('orderId', order_id),
          ('productOrderId', product_order_id),
          ('onlyValidation', 'true'),
          ('validationSuccess', 'true'),  ]
        url = 'https://sell.storefarm.naver.com/o/claim/return/' +\
              product_order_id + '/collectDone'
        resp = sess.post(url, data=data)
        return resp


def refund_confirm(account, order_info):
    with requests.Session() as sess:
        login(sess, account)
        product_order_id, order_id = order_info.split(',')
        data = [('orderId', order_id),
          ('productOrderId', product_order_id),
          ('onlyValidation', 'true'),
          ('validationSuccess', 'true'),  ]
        url = 'https://sell.storefarm.naver.com/o/claim/return/' +\
              product_order_id + '/refund'
        resp = sess.post(url, data=data)
        return resp


def exchange_collect_done(account, order_info):
    with requests.Session() as sess:
        login(sess, account)
        product_order_id, order_id = order_info.split(',')
        data = [
          ('orderId', order_id),
          ('productOrderId', product_order_id),
          ('onlyValidation', 'true'),
          ('validationSuccess', 'true'),
        ]
        url = 'https://sell.storefarm.naver.com/o/claim/exchange/' +\
              product_order_id + '/collectDone'
        resp = sess.post(url, data=data)
        pprint(resp.text)
        return resp


def exchange_confirm(account, order_info, company, invoice):
    with requests.Session() as sess:
        login(sess, account)
        product_order_id, order_id = order_info.split(',')
        data = [
          ('invoiceNo', invoice),
          ('serviceCompanyCode', company),
          ('deliveryMethod', 'DELIVERY'),
          ('orderId', order_id),
          ('claimType', 'undefined'),
          ('productOrderIds', product_order_id),
          ('onlyValidation', 'true'),
          ('validationSuccess', 'true'),
        ]
        resp = sess.post(
            'https://sell.storefarm.naver.com/o/claim/exchange/redeliveryBySelection',
            data=data)
        return resp


from datetime import datetime
def fromtimestamp(epoch, tz):
    return datetime.fromtimestamp(epoch//1000, tz=tz)


def attach_local_datetime(entries, tz, stage):
    for entry in entries:
        if stage == 'deliverstatus':
            dt1 = fromtimestamp(entry['PRODUCT_ORDER_PAY_YMDT'], tz)
            entry['datetime__'] = dt1
            entry['PRODUCT_ORDER_PAY_YMDT'] = dt1.strftime('%Y-%m-%d %H:%M:%S')
            dt2 = fromtimestamp(entry['PRODUCT_ORDER_DISPATCH_OPERATION_YMDT'], tz)
            entry['PRODUCT_ORDER_DISPATCH_OPERATION_YMDT'] =\
                              dt2.strftime('%Y-%m-%d %H:%M:%S')
        else:
            dt = fromtimestamp(entry['PAY_PAY_YMDT'], tz)
            entry['datetime__'] = dt
            entry['PAY_PAY_YMDT'] = dt.strftime('%Y-%m-%d %H:%M:%S')
            if stage == 'cancel':
                entry['CLAIM_REQUEST_OPERATION_YMDT_CANCEL'] = fromtimestamp(
                    entry['CLAIM_REQUEST_OPERATION_YMDT_CANCEL'],
                    tz).strftime('%Y-%m-%d %H:%M:%S')
            elif stage == 'refund':
                entry['CLAIM_REQUEST_OPERATION_YMDT_RETURN'] = fromtimestamp(
                    entry['CLAIM_REQUEST_OPERATION_YMDT_RETURN'],
                    tz).strftime('%Y-%m-%d %H:%M:%S')
            elif stage == 'exchange':
                entry['CLAIM_REQUEST_OPERATION_YMDT_EXCHANGE'] = fromtimestamp(
                    entry['CLAIM_REQUEST_OPERATION_YMDT_EXCHANGE'],
                    tz).strftime('%Y-%m-%d %H:%M:%S')
