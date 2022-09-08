import requests
import json
from urllib.parse import urlencode
from urllib.request import urlopen
##############################
# 使用urllib get 请求
##############################
url = 'http://127.0.0.1:8080'
print(urlopen(url))  # 返回http.client.HTTPResponse object
print(urlopen(url).read().decode())  # 返回get到的页面的源代码
print("*"*30)
# decode是将base类型转为encoding 指定的编码格式解码字符串，不指定则转为默认编码，如utf-8

##############################
# 使用urllib post请求
##############################
# 发送表单请求
url = 'http://127.0.0.1:8080/logincheck'
data = {'name': 'testuser1', 'password': '111111'}
s = urlencode(data)
res = urlopen(url, s.encode())  # post请求
print(res.read().decode())
print("*"*30)
print("#"*50)

##############################
# 使用equests get & post请求
##############################
# get请求
url = 'http://127.0.0.1:8080'
res = requests.get(url)
print(res.text)
print("*"*30)
# 表单post请求
url = 'http://127.0.0.1:8080/logincheck'
data = {'name': 'testuser1', 'password': '111111'}
res = requests.post(url, data)
print(res.text)
print("*"*30)
# json post请求
url = 'http://127.0.0.1:8080/logincheck'
data = {'name': 'testuser1', 'password': '111111'}
string = json.dumps(data)
res = requests.post(url, data)
print(res.text)
print("*"*30)
