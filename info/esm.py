import requests
import json
import sys
from pprint import pprint
from scrapy.selector import Selector

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

# 신규주문
neworder_data = [
  ('page', '1'),
  ('limit', '20'),
  ('siteGbn', '0'),
  # ('searchAccount', '341270'),
  ('searchDateType', 'ODD'),    # Ordered Day
  ('searchSDT', '2017-07-10'),
  ('searchEDT', '2017-08-10'),
  ('searchKey', 'ON'),
  ('searchKeyword', ''),
  ('searchDistrType', 'AL'),
  ('searchAllYn', 'Y'),
  ('SortFeild', 'PayDate'),
  ('SortType', 'Desc'),
  ('start', '0'),
  ('transPolicyNo', '0'),
]

# 발송처리
delivery_data = [
  ('page', '1'),
  ('limit', '100'),
  ('siteGbn', '0'),
  # ('searchAccount', '341270'),
  ('searchDateType', 'ODD'),
  ('searchSDT', '2017-05-11'),
  ('searchEDT', '2017-08-11'),
  ('searchKey', 'ON'),
  ('searchKeyword', ''),
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
  ('transPolicyNo', '0'),
]

# 배송중
sending_data = [
  ('page', '1'),
  ('limit', '20'),
  ('siteGbn', '0'),
  # ('searchAccount', '341270'),
  ('searchDateType', 'ODD'),
  ('searchSDT', '2017-06-11'),
  ('searchEDT', '2017-08-11'),
  ('searchKey', 'ON'),
  ('searchKeyword', ''),
  ('searchType', '0'),
  ('excelInfo', 'undefined'),
  ('searchStatus', '0'),
  ('searchAllYn', 'N'),
  ('SortFeild', 'PayDate'),
  ('SortType', 'Desc'),
  ('start', '0'),
  ('searchDistrType', 'AL'),
]

# Returns account number
def login(sess, id, pw, site):
    login_data = [
        ('Password', pw),
        ('ReturnUrl', ''),
        ('Id', id),
        ('RememberMe', 'true'),
        ('RememberMe', 'false'),
    ]

    if site == "esm":
        login_data.append( ('Type', 'E') )
    else:
        login_data.append( ('Type', 'S') )
        if site == "g":
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

# To do: add options in search
def get_neworder(id, pw, site):
    with requests.Session() as sess:
        account = login(sess, id, pw, site)
        neworder_data.append( ('searchAccount', account) )
        neworder_resp = sess.post('https://www.esmplus.com/Escrow/Order/NewOrderSearch',
                  headers=headers, data=neworder_data)

        return json.loads(neworder_resp.text)


    # delivery_data.append( ('searchAccount', account) )
    # sending_data.append( ('searchAccount', account) )

    # 발송처리
    # delivery_resp = sess.post('https://www.esmplus.com/Escrow/Delivery/GeneralDeliverySearch',
    #           headers=headers, data=delivery_data)
    # # 배송중
    # sending_resp = sess.post('https://www.esmplus.com/Escrow/Delivery/GetSendingSearch',
    #           headers=headers, data=sending_data)

    # delivery = json.loads(delivery_resp.text)
    # sending = json.loads(sending_resp.text)
