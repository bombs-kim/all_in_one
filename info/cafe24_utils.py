import re
noquote = re.compile(r'( id=(?=[^\'"]))')

# to deal with cafe24's funny tricks
def purify(html):
    return noquote.sub(r"\1'", html)

# a = sel.xpath("//tbody[contains(@class, 'center')]")[0]
# 주문일: a.xpath(".//td[1]")
# 주문번호: a.xpath(".//td[2]")
# 주문자: a.xpath(".//td[3]")
