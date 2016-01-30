#!/usr/bin/env python
# utf-8

'''
usage: 在修改读者卡号和密码后, 直接运行: python3 shoutu_wifi.py

'''

from urllib import parse
from urllib import request
from time import sleep
import re
import subprocess
import os

ACCOUNT = '000120162355'
PASSWORD = '194910'



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

def check_connect():
    fnull = open(os.devnull, 'w')
    data = subprocess.call('ping -c 1 www.baidu.com', shell = True, stdout=fnull, stderr=fnull)
    if data:
        return False
    else:
        return True

# main program
if __name__ == "__main__":
    login()
    while True:
        state = check_connect()
        if state:
            print('already connected')
            sleep(60)
        else:
            login()
            print('connect succeed')

