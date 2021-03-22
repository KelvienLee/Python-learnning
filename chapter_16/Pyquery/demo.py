import requests
from pyquery import PyQuery as pq

url = 'http://8.135.6.248'

r = requests.get(url)
html_content = r.text

# 使用字符串方式初始化
doc = pq(html_content)

# URL方式初始化
# 对于一些普通网站，可以直接使用pq获取网页内容
# pq_content = pq(url)
# print(pq_content)

# 文件初始化，直接传入本地文件
# file_doc = pq(filename='file_name.html')

# 查找节点
# 父节点
# print(doc('.banner-news ul li').add_class('banner-news-title'))
links = doc('.banner-news ul li a')

for item in links.items():
    print(item.attr('href'))






