from bs4 import BeautifulSoup
import requests
import lxml
import bs4
from fake_useragent import UserAgent

url = 'http://8.135.6.248/index.php?s=/index/search/goodslist.html'
ua = UserAgent()
user_agent = ua.random
print(user_agent)
exit()
try:
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': user_agent
    }
    data = {
        'category_id': '0',
        'wd': '手机',
        'page': '1',
        'order_by_field': 'default',
        'order_by_type': 'asc'
    }
    response = requests.post(url, data=data, headers=headers)
except RuntimeError:
    print('请求失败')


result = response.json()
html_content = result['data']['data']
soup = BeautifulSoup(html_content, 'lxml')
li = soup.select('.am-animation-scale-up')
list_phone = []
dict_phone = {}
for item in li:
    dict_phone['title'] = item.find('p', {'class': 'goods-title'}).string
    dict_phone['price'] = item.select_one('.price strong').string
    dict_phone['sales_count'] = item.find('span', {'class': 'sales-count'}).string
    list_phone.append(dict_phone)
print(list_phone)












