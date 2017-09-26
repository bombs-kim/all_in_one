import requests
import io
from lxml.html import parse, submit_form
from datetime import datetime
from scrapy import Selector
from pprint import pprint


headers = {
    'origin': 'https://eclogin.cafe24.com',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8,ko;q=0.6',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'referer': 'https://eclogin.cafe24.com/Shop/',
    'authority': 'eclogin.cafe24.com',
    'x-requested-with': 'XMLHttpRequest',}


def login(sess, account):
    headers = {
        'origin': 'https://eclogin.cafe24.com',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.8,ko;q=0.6',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'referer': 'https://eclogin.cafe24.com/Shop/',
        'authority': 'eclogin.cafe24.com',
        'x-requested-with': 'XMLHttpRequest',}
    params = (
        ('url', 'MallUseAuth'),  )
    data = [
      ('mall_id', account.userid),
      ('userid', account.userid),  ]
    sess.post('https://eclogin.cafe24.com/Shop/',
                  headers=headers, params=params, data=data)
    data = [
        ('url', 'Run'),
        ('IS_DEVSERVER', ''),
        ('login_mode', '1'),
        ('use_second_auth', 'F'),
        ('second_auth_method', ''),
        ('caller_id', ''),
        ('userid', account.userid),
        ('mall_id', account.userid),
        ('check1', 'on'),
        ('userpasswd', account.password),
        ('auth_number', ''),
        ('onnode', ''),
        ('submenu', ''),
        ('menu', ''),
        ('mode', ''),
        ('c_name', ''),
        ('loan_type', ''),
        ('addsvc_suburl', ''),
        ('is_multi', 'F'),
        ('appID', ''),
        ]
    index_resp = sess.post('https://eclogin.cafe24.com/Shop/index.php',
                  headers=headers, data=data)

    stream = io.StringIO(index_resp.text)
    form = parse(stream).getroot().xpath('//form')[0]
    check_resp = sess.post(form.action, data=dict(form.fields))

    stream = io.StringIO(index_resp.text)
    form = parse(stream).getroot().xpath('//form')[0]
    com_resp = sess.post(form.action, data=dict(form.fields))

    stream = io.StringIO(com_resp.text)
    form = parse(stream).getroot().xpath('//form')[0]
    check2_resp = sess.post(form.action, data=dict(form.fields))

    text = check2_resp.text
    text = text[text.index('>')+1:]
    text = text[text.index("'")+1:]
    url = text[:text.index("'")]
    sess.get('https://truetech02.cafe24.com/admin/php/user_id_check.php' + url)


cafe24_search_type_from_key = {
    '': None,  # default
    'ON': None,
    'GN': None,  # Not supported for cafe24
    'BN': 'o_name',
    'BI': 'member_id',
    }

get_storefarm_status_from_stage = {
    'neworder': 'NEW_ORDER',
    'deliver': 'PLACE_ORDER',
    'deliver_release': 'PLACE_ORDER_RELEASE',
}



def get_search_condition(stage, start, end, searchKey, searchKeyword):
    msk = cafe24_search_type_from_key[searchKey]
    if not msk:
        msk = 'order_id'
        searchKeyword = ''
    if stage == 'neworder':
        data = [
          ('realclick', 'T'),
          ('tabclick', 'F'),
          ('listKeyType', 'om_no'),
          ('print_select_nos', ''),
          ('listType', ''),
          ('keyType', 'om_no'),
          ('queryString', ''),
          ('isOpenMarketCancled', ''),
          ('bPrdPrepareUse', '1'),
          ('bExpressFlag', ''),
          ('excel_private_auth', 'T'),
          ('excel_public_auth', 'T'),
          ('navi_hide', ''),
          ('searchPage', 'shipped_begin_list'),
          ('menu_no', '72'),
          ('sSearchDetailView', 'F'),
          ('sSearchDetailStretch', 'F'),
          ('searched_shop_no', '1'),
          ('sIsBusanCallCenter', ''),
          ('sOrderSearchLimit', ''),
          ('MSK[]', msk),
          ('MSV[]', searchKeyword),
          ('date_type', 'pay_date'),
          ('start_date', start),
          ('btnDate', '7'),
          ('year1', start[:4]),
          ('month1', start[5:7]),
          ('day1', start[8:10]),
          ('end_date', end),
          ('year2', end[:4]),
          ('month2', end[5:7]),
          ('day2', end[8:10]),
          ('today', datetime.now().strftime("%Y-%m-%d")),
          ('product_search_type', 'product_name'),
          ('order_product_text', ''),
          ('order_product_no', ''),
          ('find_option', 'product_no'),
          ('memberType', '1'),
          ('shipment_type', 'all'),
          ('paystandard', 'choice'),
          ('product_total_price1', ''),
          ('product_total_price2', ''),
          ('item_count', 'all'),
          ('saleMarketCheck', 'on'),
          ('inflowChannelCheck', 'on'),
          ('paymethod_total_count', '21'),
          ('discountMethodCheck', 'on'),
          ('fPGMethodCheck', 'on'),
          ('search_SaleOpenMarket[]', 'cafe24'),
          ('search_SaleOpenMarket[]', 'mobile'),
          ('search_SaleOpenMarket[]', 'mobile_d'),
          ('search_SaleOpenMarket[]', 'NCHECKOUT'),
          ('search_SaleOpenMarket[]', 'INTERPARK'),
          ('search_SaleOpenMarket[]', 'auction'),
          ('search_SaleOpenMarket[]', 'sk11st'),
          ('search_SaleOpenMarket[]', 'gmarket'),
          ('search_SaleOpenMarket[]', 'coupang'),
          ('search_SaleOpenMarket[]', 'shopn'),
          ('search_SaleOpenMarket[]', 'auction_os'),
          ('search_SaleOpenMarket[]', 'INTERPARK_OS'),
          ('search_SaleOpenMarket[]', 'naver_ks'),
          ('search_SaleOpenMarket[]', 'live_link_on'),
          ('search_SaleOpenMarket[]', 'etc'),
          ('paymentMethod[]', 'cash'),
          ('paymentMethod[]', 'card'),
          ('paymentMethod[]', 'tcash'),
          ('paymentMethod[]', 'cell'),
          ('paymentMethod[]', 'icash'),
          ('paymentMethod[]', 'esc_rcash'),
          ('paymentMethod[]', 'esc_icash'),
          ('paymentMethod[]', 'esc_vcash'),
          ('paymentMethod[]', 'kpay||card'),
          ('paymentMethod[]', 'paynow||card'),
          ('paymentMethod[]', 'paynow||tcash'),
          ('paymentMethod[]', 'payco||card'),
          ('paymentMethod[]', 'payco||esc_rcash'),
          ('paymentMethod[]', 'payco||esc_icash'),
          ('paymentMethod[]', 'payco||point'),
          ('paymentMethod[]', 'kakaopay||card'),
          ('paymentMethod[]', 'mileage'),
          ('paymentMethod[]', 'deposit'),
          ('paymentMethod[]', 'npoint'),
          ('paymentMethod[]', 'ncash'),
          ('paymentMethod[]', 'cashondelv'),
          ('discountMethod[]', 'mileage'),
          ('discountMethod[]', 'deposit'),
          ('discountMethod[]', 'coupon'),
          ('discountMethod[]', 'nmileage'),
          ('discountMethod[]', 'ncash'),
          ('fPaymentMethod[]', 'paypal'),
          ('fPaymentMethod[]', 'alipay'),
          ('fPaymentMethod[]', 'axes'),
          ('fPaymentMethod[]', 'axes_over'),
          ('fPaymentMethod[]', 'eximbay'),
          ('fPaymentMethod[]', 'tenpay'),
          ('fPaymentMethod[]', 'softbank'),
          ('fPaymentMethod[]', 'ecpay'),
          ('deferPaymentMethod[]', 'npdefer'),
          ('deferPaymentMethod[]', 'gmodefer'),
          ('deferPaymentMethod[]', 'daibiki'),
          ('deferPaymentMethod[]', 'huodaofukuan'),
          ('main_search', ''),
          ('searchTimeUsed', 'F'),
          ('mkSaleTypeChg', ''),
          ('mkSaleType', 'M'),
          ('inflowPathDetail', '0000000000000000000000000000000000'),
          ('searchSorting', 'pay_date_asc'),
          ('rows', '100'),
          ('shop_no_excel', '1'),
          ('userfile', ''),
          ('bIsMultiShop', ''),
          ('radio10', 'on'),
          ('radio11', 'on'),
          ('radio12', 'on'),
          ('radio100', 'on'),
        ]
    if stage == 'deliver':
        data = [
          ('realclick', 'T'),
          ('tabclick', 'F'),
          ('listKeyType', 'om_no'),
          ('print_select_nos', ''),
          ('listType', ''),
          ('keyType', 'om_no'),
          ('queryString', ''),
          ('isOpenMarketCancled', ''),
          ('bPrdPrepareUse', '1'),
          ('bExpressFlag', ''),
          ('excel_private_auth', 'T'),
          ('excel_public_auth', 'T'),
          ('navi_hide', ''),
          ('searchPage', 'shipped_begin_list'),
          ('menu_no', '72'),
          ('sSearchDetailView', 'F'),
          ('sSearchDetailStretch', 'F'),
          ('searched_shop_no', '1'),
          ('sIsBusanCallCenter', ''),
          ('sOrderSearchLimit', ''),
          ('MSK[]', msk),
          ('MSV[]', searchKeyword),
          ('date_type', 'pay_date'),
          ('start_date', start),
          ('btnDate', '7'),
          ('year1', start[:4]),
          ('month1', start[5:7]),
          ('day1', start[8:10]),
          ('end_date', end),
          ('year2', end[:4]),
          ('month2', end[5:7]),
          ('day2', end[8:10]),
          ('today', datetime.now().strftime("%Y-%m-%d")),
          ('product_search_type', 'product_name'),
          ('order_product_text', ''),
          ('order_product_no', ''),
          ('find_option', 'product_no'),
          ('memberType', '1'),
          ('shipment_type', 'all'),
          ('paystandard', 'choice'),
          ('product_total_price1', ''),
          ('product_total_price2', ''),
          ('item_count', 'all'),
          ('saleMarketCheck', 'on'),
          ('inflowChannelCheck', 'on'),
          ('paymethod_total_count', '21'),
          ('discountMethodCheck', 'on'),
          ('fPGMethodCheck', 'on'),
          ('search_SaleOpenMarket[]', 'cafe24'),
          ('search_SaleOpenMarket[]', 'mobile'),
          ('search_SaleOpenMarket[]', 'mobile_d'),
          ('search_SaleOpenMarket[]', 'NCHECKOUT'),
          ('search_SaleOpenMarket[]', 'INTERPARK'),
          ('search_SaleOpenMarket[]', 'auction'),
          ('search_SaleOpenMarket[]', 'sk11st'),
          ('search_SaleOpenMarket[]', 'gmarket'),
          ('search_SaleOpenMarket[]', 'coupang'),
          ('search_SaleOpenMarket[]', 'shopn'),
          ('search_SaleOpenMarket[]', 'auction_os'),
          ('search_SaleOpenMarket[]', 'INTERPARK_OS'),
          ('search_SaleOpenMarket[]', 'naver_ks'),
          ('search_SaleOpenMarket[]', 'live_link_on'),
          ('search_SaleOpenMarket[]', 'etc'),
          ('paymentMethod[]', 'cash'),
          ('paymentMethod[]', 'card'),
          ('paymentMethod[]', 'tcash'),
          ('paymentMethod[]', 'cell'),
          ('paymentMethod[]', 'icash'),
          ('paymentMethod[]', 'esc_rcash'),
          ('paymentMethod[]', 'esc_icash'),
          ('paymentMethod[]', 'esc_vcash'),
          ('paymentMethod[]', 'kpay||card'),
          ('paymentMethod[]', 'paynow||card'),
          ('paymentMethod[]', 'paynow||tcash'),
          ('paymentMethod[]', 'payco||card'),
          ('paymentMethod[]', 'payco||esc_rcash'),
          ('paymentMethod[]', 'payco||esc_icash'),
          ('paymentMethod[]', 'payco||point'),
          ('paymentMethod[]', 'kakaopay||card'),
          ('paymentMethod[]', 'mileage'),
          ('paymentMethod[]', 'deposit'),
          ('paymentMethod[]', 'npoint'),
          ('paymentMethod[]', 'ncash'),
          ('paymentMethod[]', 'cashondelv'),
          ('discountMethod[]', 'mileage'),
          ('discountMethod[]', 'deposit'),
          ('discountMethod[]', 'coupon'),
          ('discountMethod[]', 'nmileage'),
          ('discountMethod[]', 'ncash'),
          ('fPaymentMethod[]', 'paypal'),
          ('fPaymentMethod[]', 'alipay'),
          ('fPaymentMethod[]', 'axes'),
          ('fPaymentMethod[]', 'axes_over'),
          ('fPaymentMethod[]', 'eximbay'),
          ('fPaymentMethod[]', 'tenpay'),
          ('fPaymentMethod[]', 'softbank'),
          ('fPaymentMethod[]', 'ecpay'),
          ('deferPaymentMethod[]', 'npdefer'),
          ('deferPaymentMethod[]', 'gmodefer'),
          ('deferPaymentMethod[]', 'daibiki'),
          ('deferPaymentMethod[]', 'huodaofukuan'),
          ('main_search', ''),
          ('searchTimeUsed', 'F'),
          ('mkSaleTypeChg', ''),
          ('mkSaleType', 'M'),
          ('inflowPathDetail', '0000000000000000000000000000000000'),
          ('searchSorting', 'pay_date_asc'),
          ('rows', '100'),
          ('shop_no_excel', '1'),
          ('userfile', ''),
          ('bIsMultiShop', ''),
          ('radio10', 'on'),
          ('radio11', 'on'),
          ('radio12', 'on'),
          ('radio100', 'on'),
        ]

    return data

search_urls = {
    'neworder': 'https://truetech02.cafe24.com/admin/php/shop1/s_new/product_prepare_list_ord_num.php',
    'deliver': 'https://truetech02.cafe24.com/admin/php/shop1/s_new/shipped_begin_list.php'
}

def search(account, stage, start, end,
                 searchKey='', searchKeyword=''):
    start = start.strftime("%Y-%m-%d")
    end = end.strftime("%Y-%m-%d")

    with requests.Session() as sess:
        login(sess, account)
        data = get_search_condition(
            stage, start, end, searchKey, searchKeyword)
        data.append(
            ('mallId', account.userid) )

        resp = sess.post(search_urls[stage],
             headers=headers, data=data)
    return extract_entries(resp, stage)

def text_without_whitespaces(sel):
    ts = sel.xpath('.//text()').extract()
    ret = ''
    for t in ts:
        ret += t.strip()
    return ret

def extract_entries(response, stage):
    sel = Selector(text=response.text)
    entries = []

    if stage == 'neworder':
        tr = sel.xpath("//table[@id='shipedReadyList']//tr")
        for td in tr[1:]:
            td = td.xpath(".//td")
            entry = {}
            order_date = text_without_whitespaces(td[1])
            entry['OrderDate'] = order_date[:order_date.find('(')]
            entry['OrderNo'] = text_without_whitespaces(td[2])
            entry['BuyerID'] = td[3].xpath('span/text()')[0].extract()
            # 묶음선택 4
            # some checkbox 5
            entry['Supplier'] = text_without_whitespaces(td[6])
            entry['Product'] = text_without_whitespaces(td[7])[19:]
            entry['Quantity'] = text_without_whitespaces(td[8])
            entry['Price'] = text_without_whitespaces(td[10])
            entry['ActualPrice'] = text_without_whitespaces(td[13])
            entry['Method'] = td[14].xpath('.//img/@title')[0].extract()
            entry['Addr'] = 'None [Cafe24]'
            entries.append(entry)
    if stage == 'deliver':
        tables = sel.xpath('//*[@id="shipedReadyList"]/table')
        # return tables, tables
        for tbl in tables[1:]:
            td = tbl.xpath(".//tr[1]//td")
            entry = {}
            order_date = text_without_whitespaces(td[1])
            entry['OrderDate'] = order_date[:order_date.find('(')]
            entry['OrderNo'] = text_without_whitespaces(td[2])
            entry['BuyerID'] = td[3].xpath('span/text()')[0].extract()
            # 묶음선택 4
            # some checkbox 5
            # 운송장정보 6
            entry['DeliveryFee'] = td[7].xpath(".//input/@value")[0].extract()  # 처음에 무조건 0으로 되어있는 듯 보임
            entry['Supplier'] = text_without_whitespaces(td[8])
            entry['Product'] = text_without_whitespaces(td[9])[19:]
            entry['Quantity'] = text_without_whitespaces(td[10])
            entry['Price'] = text_without_whitespaces(td[12])
            entry['ActualPrice'] = text_without_whitespaces(td[15])
            entry['Method'] = td[16].xpath('.//img/@title')[0].extract()
            entry['Addr'] = text_without_whitespaces(
                tbl.xpath(".//tr[2]//td"))
            entries.append(entry)

    return entries

#
# from datetime import datetime, timedelta
# a= lambda:None
# a.userid = "truetech02"
# a.password="true3251"
# start = datetime.now() - timedelta(days=10)
# end = datetime.now()
# stage = 'deliver'
# td, entries = search(a, stage, start, end)
