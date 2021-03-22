import requests
from fake_useragent import UserAgent

# url = 'https://httpbin.org/'
# username = input('username:')
# password = input('password:')
# age = input('age:')
# payload = {
#     'username': username,
#     'password': password,
#     'age': age
# }

# get请求带参数
# response = requests.get(url, params=payload)

# post请求带参数,数据不会被显示在网址中
# response = requests.post(url, data=payload)
# print(response)
# print(response.url)

# 添加请求头
# headers = {
# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
# }
# response = requests.get(url, headers=headers)
# print(response)
# print(response.url)

# 伪造请求头
# ua = UserAgent(verify_ssl=False)
# user_agent = ua.random
# headers = {
#     'User-Agent': user_agent
# }
# response = requests.get(url, headers=headers)
# print(response)
# print(dir(response))
# print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.text)

pic_url = "https://cdn.pixabay.com/photo/2018/06/25/00/51/sunrise-3495775_960_720.jpg"
response = requests.get(pic_url)
try:
    response = requests.get(pic_url)
except RuntimeError:
    print('无法请求')
else:
    # print(response.content)
    with open('pic.jpg', 'wb') as f:
        f.write(response.content)










