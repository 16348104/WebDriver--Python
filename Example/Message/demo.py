import requests
import urllib
import time

appkey = '5c8cd448cf2cb4646e56c214a6519b6d'  # 固定的不变，请勿泄露
mobile = ''  # 短信接受者的手机号码
tpl_id = '217252'  # 固定的不变
errorMsg = '响应时间超长（错误信息xxxx）'  # 根据实际情况修改

now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
tpl_value = '#time#=' + str(now_time) + '&#server#=网络学堂&#reason#=' + errorMsg
params = 'key=%s&mobile=%s&tpl_id=%s&tpl_value=%s' % (appkey, mobile, tpl_id, urllib.parse.quote(tpl_value))
response = requests.get("https://v.juhe.cn/sms/send?" + params)
print(response.text)


#!/usr/bin/python
# -*- coding: utf-8 -*-
# import json, urllib
# from urllib import urlencode
#
# url = "http://v.juhe.cn/sms/send"
# params = {
#     "mobile": "13429667914",  # 接受短信的用户手机号码
#     "tpl_id": "111",  # 您申请的短信模板ID，根据实际情况修改
#     "tpl_value": "#code#=1235231",  # 您设置的模板变量，根据实际情况修改
#     "key": "您申请的ApiKey",  # 应用APPKEY(应用详细页查询)
# }
# params = urlencode(params)
# f = urllib.urlopen(url, params)
# content = f.read()
# res = json.loads(content)
# if res:
#     print(res)
# else:
#     print("请求异常")