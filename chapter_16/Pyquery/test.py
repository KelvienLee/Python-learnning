import requests
import re

url = 'http://8.135.6.248/'
r = requests.get(url)
html_text = r.text
# print(html_text)

# match方法，从全文
regular = '.*<b class="goods-price" data-original-price="356.00">(.*?)</b>'
# # 规则，目标内容，参数（示例为匹配所有内容，包括换行符）
content = re.match(regular, html_text, re.S)
print(content)
print(content.group(1))

# # search方法，全文搜索，不用全文匹配。
regular_search = '<b class="goods-price" data-original-price="356.00">(.*?)</b>'
content_search = re.search(regular_search, html_text, re.S)
print(content_search)
print(content_search.group(1))

# findall()匹配所有
regular_findall = '<div class="goods-items">(.*?)</p>'
content_findall = re.findall(regular_findall, html_text, re.S)
# print(content_findall)
for item in content_findall:
    # 使用sub()替换内容
    item = re.sub(r'\s+', '', item)
    print(item)


# compile()
day1 = '2021-07-18 22:34'
day2 = '2021-03-15 06:14'
day3 = '2021-04-13 12:15'

regular_compile = r'\d{2}:\d{2}'
# 将其编译为正则对象
pattern = re.compile(regular_compile)
print(pattern)
print(re.sub(pattern, '', day1))
print(re.sub(pattern, '', day2))
print(re.sub(pattern, '', day3))























