from bs4 import BeautifulSoup
import requests
import lxml

url = 'http://8.135.6.248/'
try:
    response = requests.get(url)
except RuntimeError:
    print('请求失败')


html_content = response.text

# BeautifulSoup类型  获取整个html文档
soup = BeautifulSoup(html_content, 'xml')
# print(soup)
# print(type(soup))
#
# # Tag类型  获取html标签
# print(soup.title)
# print(type(soup.title))
#
# # NavigableString类型，获取标签内容
# print(soup.title.string)
# print(type(soup.title.string))
#
# # 只能获取到匹配到的第一个标签
# print(soup.a)
# # 标签下还有嵌套标签的话无法获取字符串内容
# print(soup.a.string)             # 返回None


# 获取页面em标签, 获取兄弟节点
# print(soup.em)
# 获取文档原始内容（如空格等不显示的内容）
# print(repr(soup.em.next_sibling))
# print(soup.em.next_sibling.next_sibling)

# 获取em标签的父节点
# print(soup.em.parent.parent.parent)
# print(soup.em.parents)      # 返回生成器
# for item in soup.em.parents:
#     print(item)
#     print()

# find方法
# nav = soup.find('ul', {'class': 'top-nav-right'})
# # print(nav)
# for item in nav.children:
#     # print(repr(item))
#     if item != '\n':
#         print(item.span.string)


# find_all方法
# nav = soup.find_all('div', {'class': 'top-nav-items'})
# for item in nav:
#     if item.span:
#         print(item.span.string)


# select方法
nav = soup.select('.top-nav-items .login-event')
for item in nav:
    print(item.span.string)





