import re
noquote = re.compile(r'( id=(?=[^\'"]))')

# to deal with cafe24's funny tricks
def purify(html):
    return noquote.sub(r"\1'", html)

# 배송준비중 관리 (발송대기)
# e = sel.xpath("/tbody")
# 주문일: e.xpath(".//td")[1]
# 주문번호: e.xpath(".//td")[2]
# 주문자: e.xpath(".//td")[3]
# 묶음선택  4
# some checkbox 5
# 운송장정보 6
# 배송비 7 - 처음에 무조건 0으로 되어있는 듯 보임
# 공급사 8
# 상품명/옵션 9
# 수량 10
# 상품구매금액 12
# 총 실결제금액 15
# 결제수단  16
# 수령지정보 18


# 배송정보
# e = sel.xpath("//table[@id='searchResultList']")
# 주문번호 1
# 주문자 2
# 수령지정보 3
# some checkbox 4
# 배송일 5
# 택배사 6
# 공급사 7
# 상품명/옵션 8
# 수량 9


# 취소


# 교환


# 환불 - 분리가 안되어 있음 ㅅㅂ





# cafe24는 '주문확인'이 없음
