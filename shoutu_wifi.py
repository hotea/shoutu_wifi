#!/usr/bin/env python
# utf-8

'''
usage:

在修改读者卡号和密码后, 直接运行: python3 shoutu_wifi.py


这个版本登录之后验证状态使用的方法是再次登录然后查看返回页面, 有待改进

'''

from urllib import parse
from urllib import request
from time import sleep
import re

ACCOUNT = "xxxxxxxxx"
PASSWORD = "xxxxxx"


def login():
    url = 'http://dlpp.clcn.net.cn:1111/login.asp'
    userinfo = {
            'username':ACCOUNT,
            'pswd':PASSWORD
            }
    data = parse.urlencode(userinfo).encode('utf8')
    req = request.Request(url, data)
    response = request.urlopen(req).read().decode("utf8")
    return response


# main program
if __name__ == "__main__":
    while True:
        response = login()
        if re.search('在线窗口', response):
            print('登录成功')
            # sleep 29 分钟, 首图wifi 30分钟断线一次
            sleep(1740)
        elif re.search('输入的读者卡卡号或密码错误', response):
            print('帐号或密码错误')
            break
        elif re.search('用户已经在线', response):
            print('已在线')
            sleep(60)

