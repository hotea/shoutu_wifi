#!/usr/bin/env python
# utf-8

'''
usage: 在修改读者卡号和密码后, 直接运行: python3 shoutu_wifi.py
'''

from urllib import parse
from urllib import request
from urllib.error import URLError
from time import sleep
import re
import subprocess
import sys
import os
import getpass


# 如果不想每次输入密码,可在此将 ACCOUNT 和 PASSWORD 预设, 如:
# ACCOUNT = '000111222333'
# PASSWORD = '123456'
ACCOUNT = None
PASSWORD = None

def login():
    LOGIN_URL = 'http://dlpp.clcn.net.cn:1111/login.asp'
    userinfo = {
            'username':ACCOUNT,
            'pswd':PASSWORD
            }
    data = parse.urlencode(userinfo).encode('utf8')
    req = request.Request(LOGIN_URL, data)
    try:
        response = request.urlopen(req, timeout=5).read().decode("utf8")
    except URLError as e:
        print('请检查网络连接')
        sys.exit()
    if re.search('卡号或密码错误', response):
        print('卡号或密码错误, 请修改后重试')
        sys.exit()
    return True

def check_connect():
    fnull = open(os.devnull, 'w')
    data = subprocess.call('ping -c 1 www.baidu.com', shell = True, stdout=fnull, stderr=fnull)
    if data:
        return False
    else:
        return True

# main program
if __name__ == "__main__":
    try:

        if not ACCOUNT or not PASSWORD:
            if len(sys.argv) == 1:
                ACCOUNT = input('输入读者卡号: ')
                PASSWORD = getpass.getpass(prompt='输入六位数密码: ')
            elif len(sys.argv) == 2:
                ACCOUNT = sys.argv[1]
                PASSWORD = getpass.getpass(prompt='输入六位数密码: ')
            else:
                ACCOUNT = sys.argv[1]
                PASSWORD = sys.argv[2]

        if login():
            print('连接成功')
        while True:
            state = check_connect()
            if not state:
                login()
            else:
                sleep(30)
    except KeyboardInterrupt as k:
        print('退出程序...')
        sys.exit()

