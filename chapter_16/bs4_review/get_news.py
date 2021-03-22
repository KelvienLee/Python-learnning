from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests

ua = UserAgent(verify_ssl=False)
user_agent = ua.random
headers = {
    "User-Agent": user_agent
}


def get_info(url):
    try:
        response = requests.get(url, headers=headers)
        return response
    except RuntimeError:
        print('无法获取数据')


html_url = 'http://8.135.6.248'
response1 = get_info(html_url)
html_text = response1.text

# 实例化beautifulsoup4(内容，解析器）
soup = BeautifulSoup(html_text, 'lxml')

news = soup.select('.banner-news ul li a')
links = []
for item in news:
    link = item.get('href')
    links.append(link)

print(links)
exit()
# print(links)
news_list = []

for url_link in links[1:]:
    news_detail = {}
    response2 = get_info(url_link)
    html = response2.text
    soup_branch = BeautifulSoup(html, 'lxml')
    news_detail['title'] = soup_branch.find('h1', {'class': 'am-article-title'}).string
    news_detail['publish_date'] = soup_branch.select('.am-article-meta span')[0].string
    news_detail['view_count'] = soup_branch.select('.am-article-meta span')[1].string
    news_detail['content'] = soup_branch.find('div', {'class': 'am-article'}).text
    news_list.append(news_detail)


for item1 in news_list:
    print(item1)



















