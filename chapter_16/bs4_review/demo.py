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


html_url = 'http://8.135.6.248/index.php?s=/index/search/index/wd/6E98B86EC9AB.html'
response1 = get_info(html_url)
html_text = response1.text
print(html_text)

# 实例化beautifulsoup4(内容，解析器）
# soup = BeautifulSoup(html_text, 'lxml')

# 获取兄弟节点
# print(soup.em)
# print(repr(soup.em.next_sibling))
# print(soup.em.next_sibling.next_sibling)
#
# # 获取父节点
# print(soup.em.parent)
# print(soup.em.parent.parent)
#
# # 使用parents方法会获取所有的上层标签，并返回一个生成器
# # 生成的生成器可以使用遍历方法获取
# all_content = soup.em.parents
# for i in all_content:
#     print(i)

# 只有一个类标签属性的时候
# nav = soup.find('ul', class_='top-nav-right')
#
# # 如果有多个类标签
# nav_s = soup.find('ul', {'class': 'top-nav-right'})
#
# # print(nav_s)
#
# for item in nav.children:
#     # print(repr(item))
#     if item != '\n':
#         print(item.span.string)

# nav_all = soup.find_all('div', {'class': 'top-nav-items'})
# # print(nav_all)
# for item in nav_all:
#     if item.span:
#         print(item.span.string)

# nav_sel = soup.select('.top-nav-right .menu-hd')
# # print(nav_sel)
# for item in nav_sel:
#     print(item.span.string)




































