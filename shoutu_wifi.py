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
    except:
        print('未知错误,请重试')
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

def save_info(account=None, password=None):
    try:
        with open('.userinfo', 'w') as f:
            userinfo = account, password
            f.writelines(','.join(userinfo))
            return True
    except IOError:
        print('不能保存密码, 请检测文件访问权限')
        return False
    except Exception:
        sys.exit()

def load_info():
    try:
        if os.path.exists('.userinfo'):
            if os.path.getsize('.userinfo') == 0:
                return None
            else:
                with open('.userinfo', 'r') as f:
                    userinfo = tuple(f.readline().split(','))
                    return userinfo
    except Exception as e:
        sys.exit()

# main program
if __name__ == "__main__":
    try:
        info = load_info()
        if info:
            ACCOUNT, PASSWORD = info
        else:
            ACCOUNT = input('输入读者卡号: ')
            PASSWORD = getpass.getpass(prompt='输入六位数密码: ')
            

        if login():
            if not info:
                is_save = input('是否保存密码? (y)es/(n)o:').strip().lower() 
                if is_save == 'y' or is_save == 'yes':
                    save_info(ACCOUNT, PASSWORD)
            print('连接成功')
            print('若要退出请按 Ctrl + C ')
        while True:
            state = check_connect()
            if not state:
                login()
            else:
                sleep(30)
    except KeyboardInterrupt as k:
        print('退出程序...')
        sys.exit()
    except Exception as e:
        sys.exit()

