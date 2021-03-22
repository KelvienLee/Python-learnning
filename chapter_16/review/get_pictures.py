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


pic_url = 'https://tjg.hywly.com/a/1/36222/2.jpg'

pic_content = get_info(pic_url)
content = pic_content.content
with open('pic.jpg', 'wb') as pic:
    pic.write(content)
