#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'yingxue'

import base64
import hashlib
import configparser
import redis
import requests
import json
import sys
import os
import re
import subprocess
import http.client
import time
from lxml import html
import random


def sign(params, app_secret):
    params = sorted(params.iteritems(), key=lambda d: d[0])
    query_string = ''
    for eachParam, eachValue in params:
        if query_string == '':
            query_string += eachParam + '=' + str(eachValue)
        else:
            query_string += '&' + eachParam + '=' + str(eachValue)
    query_string += app_secret
    signature = hashlib.new('md5', query_string).hexdigest().upper()
    return signature


def parse_query_string(params):
    query_string = ''
    for each_key, each_value in params:
        if query_string == '':
            query_string += each_key + '=' + str(each_value)
        else:
            query_string += '&' + each_key + '=' + str(each_value)
    return query_string


def parse_query_string_of_dict(params):
    query_string = ''
    for each_key, each_value in params.items():
        if query_string == '':
            query_string += each_key + '=' + str(each_value)
        else:
            query_string += '&' + each_key + '=' + str(each_value)
    return query_string


# def encode_pass(password):
#     return base64.b64encode(
#         hashlib.new(
#             'sha1',
#             'wealthbetter' + hashlib.new('sha1', password).hexdigest()
#         ).hexdigest()
#     )




def parse_config(path='E:/soft/webtest/config/config.conf'):
    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_redis():
    # redis_connection = redis.StrictRedis(
    #     host=config.get('redis', 'host'),
    #     port=config.get('redis', 'port'),
    #     db=config.get('redis', 'db')
    # )
    redis_connection = redis.StrictRedis(host='192.168.1.158', port=6377, db = 0, decode_responses=True)
    # print(redis_connection)
    return redis_connection


def get_verify_code(mobile, request_type=1):
    config = parse_config()
    send_mobile_verify_params = {
        'mobile': mobile,
        'way': request_type
    }
    send_mobile_verify_params['authSign'] = sign(send_mobile_verify_params, config.get('interface', 'appSecret'))
    send_mobile_verify_url = config.get('interface', 'apiUrl') + 'sendMobileVerify'
    mobile_verify = requests.post(send_mobile_verify_url, send_mobile_verify_params, verify=False).text
    print(mobile_verify)
    mobile_verify = json.loads(mobile_verify)
    if mobile_verify['msg'] == 'OK':
        mobile_code = mobile_verify['data']['mobile_code'].split('_')[-1]
        return mobile_code
    return False


def get_token():
    redis_connection = get_redis()
    user_info = redis_connection.get('USER_INFO')
    if user_info is None:
        return False
    user_info = ujson.loads(user_info)
    token = user_info['data']['token']
    return token


def login():
    config = parse_config()
    api_url = config.get('interface', 'apiUrl')
    redis_connection = get_redis()
    response = redis_connection.get('USER_INFO')
    if not response:
        muname = config.get('user', 'muname')
        mupass = encode_pass(config.get('user', 'mupass'))
        login_url = api_url + 'login'
        #headers = {'user-agent': 'android-async-http/1.4.5 (http://loopj.com/android-async-http)'}
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0'}
        # headers = {'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) '
        #                          'AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 '
        #                          'MicroMessenger/4.5.255'}
        print(login_url)
        r = requests.post(login_url, {'muname': muname, 'mupass': mupass}, verify=False, headers=headers)
        # r = get(login_url, {'muname': muname, 'mupass': mupass})
        response = r.text
        if r.status_code == 200 and response:
            response_obj = json.loads(response)
            if response_obj['error_code'] == 0:
                redis_connection.set('USER_INFO', response, ex=1800)
                return response_obj
            else:
                print(response_obj['msg'])
                return False
        else:
            print("login failed")
            print(response)


def get(url, params=None):
    if params is not None:
        url += '?' + parse_query_string_of_dict(params)
    r = requests.get(url, verify=False)
    if r.status_code != 200:
        print('Error ' + str(r.status_code) + chr(10))
    else:
        print('Successfully Connected Address:' + url + '\n')
        print('The Response Data is :' + "\n\r")
        print(r.text + chr(10))
        print('The Parsed Data is :' + '\n\r')
        response = ujson.loads(r.text)
        print(response)
        return r


def post(url, params={}, files={}):
    # headers = {'basic-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0'}
    # headers = {'basic-agent':'android-async-http/1.4.5 (http://loopj.com/android-async-http)'}
    # headers = {'basic-agent': 'wealthbetter/1.2.5.1 (iPhone; iOS 7.1.1; Scale/2.00)'}
    headers = {
        'basic-agent': 'Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255'}
    if not files:
        r = requests.post(url, data=params, verify=False, headers=headers)
    else:
        r = requests.post(url, data=params, files=files, verify=False, headers=headers)
    if r.status_code != 200:
        print('Error ' + str(r.status_code) + chr(10) + str(r.text))
    else:
        print('Successfully Connected Address:' + url + '\n')
    print('The Response Data is :' + "\n\r")
    print(ujson.dumps(ujson.loads(r.text), ensure_ascii=False))
    print('The Parsed Data is :' + '\n\r')
    response = ujson.loads(r.text)
    string = var_dump(response)
    print(string)
    print(r.headers)


def var_dump(my_dict, level=1):
    my_type = type(my_dict)
    if my_type != dict and my_type != list and my_type != set and my_type != unicode and my_type != bool:
        return str(my_dict) + ','
    elif my_type == unicode:
        return '"' + str(my_dict) + '",'
    elif my_type == dict:
        final_string = '['
        for k, v in my_dict.items():
            if type(k) == unicode:
                k = '"' + k + '"'
            final_string += '\n' + level * " " + k + ' => ' + var_dump(v, level + 1 + len(k))
        if level == 1:
            return final_string + '\n' + level * " " + '];'
        else:
            return final_string + '\n' + level * " " + '],'

    elif my_type == bool:
        return str(my_dict).lower() + ','
    else:
        final_string = '[\n'
        for item in my_dict:
            final_string += level * " " + var_dump(item, level + 1) + '\n'
        if level == 1:
            return final_string + '\n' + level * " " + '];'
        else:
            return final_string + '\n' + level * " " + '],'


def ping(url):
    r = requests.get(url, verify=False)
    print(r.status_code)


def fetch(url, params={}):
    if params is not None:
        r = requests.post(url, params, verify=False)
    else:
        r = requests.get(url, verify=False)
    if r.status_code != 200:
        print('Error NO.' + r.status_code)
    else:
        print(r.text)

# def getsmscode():
#     smscode = ""
#     os.system("adb logcat -c")
#     cmd = "adb logcat -d | findstr SmsInterceptReceiver"
#     num = 0
#     while True and num < 100:
#         content = os.popen(cmd).read()
#         if len(content) > 0 and content.find(u"新浪支付") != -1:
#             smscode = re.findall(r"(\d{6}?)", content)
#             smscode = smscode[len(smscode) - 1]
#             if len(smscode) >= 6:
#                 break
#         else:
#             num += 1
#
#     return smscode

def getsmscode():
    time.sleep(6)
    smscode = ""
    cmd = "adb logcat -d | findstr SmsInterceptReceiver"
    content = os.popen(cmd).read()
    # content = subprocess.check_output(cmd.split(' '), shell=True)
    # content = os.system(cmd)
    if len(content) > 0 and content.find(u"smsCode: ") != -1:
        smscode = re.findall(r"(\d{6}?)", content)
        smscode = smscode[len(smscode) - 1]
    print("验证码：" + smsCode)
    return smscode.strip()

def clear_logcat():
    os.system("adb logcat -c")
    return


def getidcard():
    conn = http.client.HTTPConnection("192.168.1.158:8000")
    conn.request("GET", "/id.php")
    r1 = conn.getresponse()
    data2 = filter_tags(r1.read()).strip()
    conn.close()
    if r1.status == 200:
        data2 = re.search(r'\d{17}(\d|X|x)', data2).group()
        return data2
    else:
        return None

def filter_tags(htmlstr):
    s = re.sub(r'<(.|\n)+?>', '', html.tostring(htmlstr))
    return s

def get_id_card():
    areacode = [str(x) for x in range(0, 18)]
    birthday = time.strftime('%Y%m%d')
    seed = "1234567890"
    sa = ''
    for i in range(3):
        sa = sa + random.choice(seed)
    id = '1101' + '{:0>2}'.format(random.choice(areacode)) + birthday + sa
    c = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
    r = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
    total = 0
    for i in range(17):
        total = total + int(id[i]) * c[i]
    id = id + r[total % 11]
    return id

#get sms verifying code from redis
def get_sms(mobile):
    redis_con = get_redis()
    verify_code = redis_con.get("sms_verify" + mobile)
    return verify_code

def encode_pass(password):
    hash_string = 'wealthbetter' + hashlib.new('sha1', password.encode("utf8")).hexdigest()
    hashed = hashlib.new(
            'sha1',
            bytes(hash_string, encoding="utf8")
        ).hexdigest()
    return base64.b64encode(
        bytes(hashed, encoding="utf8")
    )

if __name__ == '__main__':
    login()


