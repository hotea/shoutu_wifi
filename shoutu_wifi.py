#!/usr/bin/env python

from urllib import parse
from urllib import request

url = 'http://dlpp.clcn.net.cn:1111/login.asp'
values = {
        'username':'000120162355',
        'pswd':'194910'
        }
data = parse.urlencode(values).encode('utf8')
req = request.Request(url, data)
response = request.urlopen(req)
page = response.read()
print(page.decode("utf8"))
