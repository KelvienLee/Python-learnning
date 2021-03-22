import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

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
        print('获取数据异常')


html_url = 'http://www.wenzizhan.com/article/22502.html'
root_content = get_info(html_url)
content = root_content.text

soup = BeautifulSoup(content, 'lxml')
text = soup.find('div', {'class': 'mainContent'})
text_str = str(text)
result = text_str.replace("<br/>", "").replace('<div class="mainContent">', '').replace('</div>', '')
with open('test1.txt', 'w') as test:
    test.write(result)

print('完成写入数据')


