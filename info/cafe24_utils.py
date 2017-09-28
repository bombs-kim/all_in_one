import re
noquote = re.compile(r'( id=(?=[^\'"]))')

# to deal with cafe24's funny tricks
def purify(html):
    return noquote.sub(r"\1'", html)
