import requests
from fake_useragent import UserAgent

# coding:utf-8

ua = UserAgent(verify_ssl=False)
user_agent = ua.random

headers = {
    "User-Agent": user_agent
}


def get_info(url):
    try:
        # 设置headers为默认参数
        response = requests.get(url, headers=headers)
        return response
    except RuntimeError:
        print('获取数据失败')


# 获取二进制字节类型
pic_url = 'http://weiguang19.xyz/logo.png'
response1 = get_info(pic_url)
content = response1.content
# 写入二进制文件
with open('logo.png', 'wb') as pic:
    pic.write(content)

# 获取网页文字内容
text_url = 'http://weiguang19.xyz'
response2 = get_info(text_url)
text = response2.text
with open('html.txt', 'w', encoding='utf-8') as html:
    html.write(text)























