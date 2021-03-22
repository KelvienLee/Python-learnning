# print(dir(list))

# 列表常见操作

# 1. 增
# append（）方法
# 追加在列表后面
book = ['西游记', '水浒传']
book.append('三国演义')
print(book)

# insert()方法
# 指定添加位置
book.insert(0, '红楼梦')
print(book)

# extend() 方法
# 将其他列表、元组的内容添加到既定列表
kongfu = ['天龙八部', '笑傲江湖']
book.extend(kongfu)
print(book)
print(kongfu)


# 2. 改
# 根据索引进行修改， 注意索引不能越界
book[4] = '射雕英雄传'
print(book)
# book[10] = '神雕侠侣'
# 如果索引越界则会报错
# print(book)

# 3. 查
# in: 判断元素是否在列表中，返回布尔值
# not in: 与in相反
if '红楼梦' not in book:
    print('not in')
else:
    print('in it')

# index: 查找元素的位置
# 找到第一个匹配的内容，然后就不管了，后面出现的就不会显示
print(book.index('西游记'))
book.append('红楼梦')
print(book)
print(book.index('红楼梦'))
# 元素不存在在报错    ValueError: '红楼一梦' is not in list
# print(book.index('红楼一梦'))

# count(): 查找元素的个数
# 元素不存在则返回0
print(book.count('红楼梦'))

# 4. 删
# del(): 根据索引进行删除
# 要指定 del 这一前缀命令
del book[-1]
print(book)

# pop(): 删除最后一个元素
book.pop()
print(book)

# remove(): 删除指定元素
# 如有多个元素，会删除匹配到的第一个元素
book.remove('西游记')
print(book)
book.append('水浒传')
print(book)
book.remove('水浒传')
print(book)
# 如果未匹配到元素，则会报错   ValueError: list.remove(x): x not in list
# book.remove('水浒一传')
# print(book)

# 5. 排序
list_val = [1, 3, 34, 54, 5, 645, 6, 9]
# sort(): 将list按特定顺序重新排序，默认为由小到大
list_val.sort()
print(list_val)
# 参数reverse = True 可改为倒序，由大到小
list_val.sort(reverse=True)
print(list_val)

# reverse(): 将列表倒置
list_val.reverse()
print(list_val)

# 6. 复制
# copy(): 复制一个新列表
#  列表的值是可变类型，我们可以在使用一个列表前copy一份
copied_list = list_val.copy()
print(copied_list)
print(id(list_val))
print(id(copied_list))


























