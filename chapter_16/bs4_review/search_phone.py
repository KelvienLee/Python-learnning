import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
user_agent = ua.random
headers = {
    "User-Agent": user_agent,
    "X-Requested-With": "XMLHttpRequest"
}

post_data = {
    'category_id': 0,
    'wd': '手机',
    'page': 1,
    'order_by_field': 'default',
    'order_by_type': 'asc'
}


def get_info(url):
    try:
        response = requests.get(url, headers=headers)
        return response
    except RuntimeError:
        print('请求失败')


def post_info(url):
    try:
        response = requests.post(url, data=post_data, headers=headers)
        return response
    except RuntimeError:
        print('请求失败')


html_url = 'http://8.135.6.248/index.php?s=/index/search/goodslist.html'
html_response = post_info(html_url)
html_json = html_response.json()

html_content = html_json['data']['data']
soup = BeautifulSoup(html_content, 'lxml')
li = soup.select(".am-animation-scale-up")

info_list = []
info_dict = {}
for item in li:
    info_dict['title'] = item.find('p', {'class': 'goods-title'}).string,
    info_dict['price'] = item.select_one('.price strong').string,
    info_dict['sales-count'] = item.find('span', {'class': 'sales-count'}).string
    info_list.append(info_dict)


print(info_list)
