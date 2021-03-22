# 一些学习笔记

使用 len() 函数可以获取字符串长度，返回的值是整型。

## 判断条件的省略用法
 * 数据类型                     结果
 * sir                空字符串解析为False，其余为True
 * int                0 为False，其余为True
 * Bool               False/ True

## 引入随机模块
```python

import random

user_input_number = int(input('input'))
right_number = random.randint(0, 9)

if user_input_number == right_number:
    print('you are right!')
else:
    print('you are wrong!')
    print('the right number is:', right_number)

```

## range() 和 list()函数
 range(起始值， 结束值【不含右值】，步长)函数
 list()函数可以将range()函数内的数值强制转换为列表输出
```python
value = range(0, 12)
print(list(value))

for i in range(1, 11, 2):
    print(i)
```

## 长注释被赋值到一个变量可用于输出
```python
zen = '''
给注释赋值，适合长文字的输出。
这是很长的一段注释
this is a long paragraph.
这里面的格式          会被保留。
'''
print(zen)
```

## 转义字符串的使用以及单引号和双引号的互相包裹
```python
# 转义字符的使用
# 这是一种错误的 is 使用方法，单引号会被识别为字符串标识符
# print('kelvien's hobby is creating things.')  
# 这是错误写法
# 正确的 is 使用方法是使用转义符号 \ 反斜杠 ,另外， 注意反斜杠放在前面的。解释器总是从上到下按先后顺序读取数据。
print('kelvien\'s hobby is creating things.')
# 但是，转义符号不利于代码的阅读
# 所以，正确的使用方法应该是单引号和双引号互相 ’包裹‘
print("kelvien's hobby is creating things.")
print('so, what is "creating things"?')
```

## 索引和步长的使用
```python
motto = 'so, what is "creating things"?'
love_sentence = '积善之家，必有余庆。'

print(motto[5])                 # 通过索引取得某一个具体的值
print(love_sentence[5:9])       # 切片同range()函数一样不包含右值
print(love_sentence[-5:-1])
print(love_sentence[5:])        # 5以后的所有值
print(love_sentence[-5:])
print(love_sentence[1:10:2])    # 可设置步长
```
 ###  注意事项
 1. 切片区间从小到大
 2. 切片区间左开右闭
 3. 索引越界会报错
 4. 切片越界会自动处理

## 字符串是不可变类型
#### 要给预期字符串赋上新值只有生成新的字符串变量
```python
# mutable 可变的
# immutable 不可变的
# 字符串是不可变类型
word = 'python'
print(word[0])
# word[0] = 'j'
# print(word)         # TypeError: 'str' object does not support item assignment
# 正确的改变字符串的方法是生成新的字符串变量
new_we_need = 'j' + word[1:]
print(new_we_need)

```

## 字符串常用操作方法
### 1. join()函数
#### 将字符串连接
```python
list_val = ['www', 'weiguang19', 'xyz']
str_val = '.'.join(list_val)
print(str_val)
tuple_val = ('user', 'kelvien', 'study', 'code')
str_val= '.'.join(tuple_val)
print(str_val)
```

### 2. 字符串大小写转换方法 （5种）
```python
str_val = 'I love Python!'
print(str_val.lower())                  # 全小写
print(str_val.upper())                  # 全大写
print(str_val.title())                  # 用于标题，即每个单词的第一个字母大写
print(str_val.capitalize())             # 句子的第一个字母大写
print(str_val.swapcase())               # 大小写互转
```

### 3. 字符串常用检索方法
```python
#  1. count()函数
#  区分大小写
#  str.count("被检索字符", 起始值， 结束值）   起始值和结束值可选
words = 'i love python, this is a very interesting thing!'
i = 'i'
print(words.count(i, 0, 20))

#  2. find()函数
# 返回值为该子字符串的索引位置,如果未找到就返回-1
# str.find("被检索的字符串", 检索起始位置， 检索结束位置)
j = 'v'
print(words.find(j))

# 3. index()函数
# 用法与find()函数相似
# 如果未找到结果，会返回异常
f = 'z'
# print(words.index(f))       # ValueError: substring not found

# 4. startswith() 函数
# 查询字符串是否以指定字符串开头
# 找到返回True，未找到返回False
s = 'l'
print(words.startswith(s))

# 5. endswith() 函数
# 查询字符串是否以指定字符串结尾
# 找到返回True，未找到返回False
e = '!'
print(words.endswith(e))
```
### 4. 三种字符串的分割方法
```python
# \t:制表符  \n:换行符  \r:回车 \r\n:回车换行
# 1. split()函数，默认使用 空格 \t, \n, \r 等进行分割
words = 'i love python, \nthis is a very interesting thing!'        # 标点符号与前一单词相连就会合并为一个列表元素
print(words)
print(words.split())           # 不会输出\n
print(words.split('i', 2))     # 以 i 为分割，分割为 num + 1 个（2 + 1 = 3） 共分成三个

# 2. splitlines()函数，默认使用 \n, \r, \r\n等进行分割
print(words.splitlines(True))  # 默认为False， 即输出后不包含字符串格式元素。

# 3. partition()函数
# partition() 方法用来根据指定的分隔符将字符串进行分割。
# 如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。
# partition()方法语法： var.partition(str)
# str : 指定的分隔符。
print(words.partition('o'))
```

### 5. 三种字符串的修剪方法
```python
# 1. strip()函数
# 移除字符串头尾指定的字符（默认为空格或换行符）或字符序列
# str.strip([chars[)
# chars: 指定的字符序列
words = ' !i love python, this is a very interesting thing! '           # 头尾有空格
# print(words)
# print(words.strip('!'))         #  如果指定了字符，会跳过空格再移除指定的字符
# print(words.strip())            # 未设置字符的值会默认移除空格

# 2. lstrip()函数
words1 = ' !i love python, this is a very interesting thing!'           # 头部有空格
print(words1)
print(words1.lstrip())            # 默认会移除最左边的空格（如果有空格的话）
words2 = '!i love python, this is a very interesting thing!'           # 头部没空格
print(words2)
print(words2.lstrip('!i'))        # 最左边没有空格的话，会移除最左边的指定的字符（如果没有空格）

# 3. rstrip()函数
# 同lstrip()函数
```


## 字符串格式化的方法
###  %格式化和 str.format格式化的方法已经过时
### 现推荐使用F-string的方法来格式化字符串
### 更多格式化字符串的相关内容可以查询相关帮助文档
```python
for i in range(1, 10):
    for j in range(1, i + 1):
        # print(j, '*', i, '=', j * i, end='  ')
        print(F'{j} * {i} = {j * i}', end=f'  ')
    print('\n')

# 只要使用了f-string, {}大括号内就不能出现转义符号 \ ，否则就会报错。
```


## 出现大段中文时未避免报错应：
```python
# coding:utf-8
# ^|| 将此注释放在顶部，定义中文编码为 utf-8, 可以防止中文内容过多时报错
text = '''这里有很长一段文字，为避免报错，应当使用三引号。
'''
# 为避免索引出错，开始的三引号应紧接内容，不应空格或换行，否则索引会出错
# ^|| 出现大段文字时优先使用三引号可以避免报错
```


## 检测数据类型的两种方法：
```python
food_list = ['方便面', '酸奶', '雪糕', '方便面']
print(type(food_list))
print(isinstance(food_list, list))          
# 预测是否为列表类型，如果是，返回True，否则返回False
```

## 使用id()函数可以查询数值在内存当中的位置
 ```python
list_val = [1, 3, 34, 54, 5, 645, 6, 9]
copied_list = list_val.copy()
print(copied_list)
print(id(list_val))
print(id(copied_list))
```


## 列表常见操作
```python
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

```

## 列表最简形式
```python
list_val = []
for i in range(0, 6):
    list_val.append(i ** 2)

print(list_val)

# 列表推导式
new_list = [i ** 2 for i in range(0, 6)]
print(new_list)

word_list = ['hello', 'world', 'I', 'love', 'Python']
new_list_again = [i.upper() for i in word_list]
print(new_list_again)

# 列表推导式 包含过滤条件
# 普通方法
list_val_filter = []
for i in range(21):
    if i % 2 == 0:
        list_val_filter.append(i)
print(list_val_filter)

# 列表推导式喊过滤最简形式
new_list2 = [j for j in range(21) if j % 2 == 0]
print(new_list2)

the_new_names = ['hello', 'world', 'i', 'am', 'coming']
the_list_val = []
for s in the_new_names:
    if len(s) < 3:
        the_list_val.append(s.lower())
    else:
        the_list_val.append(s.upper())
print(the_list_val)

the_new_new_files = [s.lower() if len(s) < 3 else s.upper() for s in the_new_names]
print(the_new_new_files)

# 列表推导式 循环嵌套形式
# for 循环嵌套
for_list = []
for k in '高富帅':
    for h in '白富美':
        for_list.append(k + h)
print(for_list)

the_last_list = [k + h for k in '高富帅' for h in '白富美']
print(the_last_list)

```

# 字典的相关知识
## 1. 创建字典
```python
# 创建字典
# 字典没有索引和切片
heroes = {'及时雨': '宋江', '玉麒麟': '卢俊义', '花和尚': '鲁智深', '母夜叉': '孙二娘'}
print(type(heroes))

empty_dict = dict()
print(type(empty_dict))

hero_star = {'天罡星': {'及时雨': '宋江', '玉麒麟': '卢俊义'},
             '地煞星': {'花和尚': '鲁智深'}}

print(heroes['花和尚'])
print(hero_star['天罡星']['玉麒麟'])
print(hero_star['天罡星']['及时雨'])

# 如果键名相同，会默认取最后一个值
# 所以一个字典中不要使用相同的键名
dict_val = {'黑旋风': '李逵', '黑旋风': '李鬼'}
print(dict_val['黑旋风'])

# 键值可以相同
dict_val2 = {'及时雨': '宋江', '呼保义':'宋江', '忠义黑三郎': '宋江'}
print(dict_val2['及时雨'])
print(dict_val2['呼保义'])
print(dict_val2['忠义黑三郎'])
```

## 2. 字典的常见操作
```python
# 1. 新增数据
heroes = {'及时雨': '宋江', '玉麒麟': '卢俊义', '花和尚': '鲁智深', '母夜叉': '孙二娘'}
heroes['豹子头'] = '林冲'
print(heroes)

# 2. 修改数据
heroes['及时雨'] = '宋公明'
print(heroes)

# update() 将新的字典的值添加到另一字典当中
# 如果新的字典里有值与既定字典的值相同，则不会添加进去
# 如果新字典的值发生改变，则会覆盖既定字典的值
more_heroes = {'黑旋风': '李逵', '入云龙': '公孙胜'}
heroes.update(more_heroes)
print(heroes)

# 3. 删除操作
# del()
# 删除一个元素
del heroes['及时雨']
print(heroes)
# 删除整个字典
# del heroes
# print(heroes)   NameError: name 'heroes' is not defined

# pop()     根据键名删除指定元素
heroes.pop('花和尚')
print(heroes)
# 如果键名不存在则会出现错误
# heroes.pop('麒麟')
# print(heroes)   KeyError: '麒麟'

# popitem() 删除最后一个元素
heroes.popitem()
print(heroes)

# clear() 删除整个字典的所有元素，并保留空字典
# heroes.clear()
# print(heroes)


# 4. 查询列表
# 根据键名进行查询
if '豹子头' in heroes:
    print('in')
else:
    print('not in')

# 5. 字典取值
# key()
# 取出键名
keys = heroes.keys()
print(keys)
print(list(keys))
for key in keys:
    print(key)

# values()
# 取出键值
hero_val = heroes.values()
print(hero_val)
print(list(hero_val))
for val_key in hero_val:
    print(val_key)

# items()
items = heroes.items()
print(items)
print(list(items))
print(list(items)[0])
# 利用元组拆包拆分字典
t_key, t_value = list(items)[0]
print(t_key)
print(t_value)
# for item_val in items:
#     print(item_val)

# 6. 字典复制
# copy()
# 字典是可变类型 可使用copy()函数保存副本
heroes_copy = heroes.copy()

```

## 3. 字典的遍历
```python
# 遍历 key
heroes = {'及时雨': '宋江', '玉麒麟': '卢俊义', '花和尚': '鲁智深', '母夜叉': '孙二娘'}
keys = heroes.keys()
for key in keys:
    print(key)


# 遍历 value
values = heroes.values()
for value in values:
    print(value)

# 遍历 item
# 返回元组
items = heroes.items()
print(items)
for item in items:
    print(item)

# 遍历 key-value
item_val = heroes.items()
print(item_val)
for key_val, value_key in item_val:
    print(F'{key_val} => {value_key}')

```

## 集合相关
### 1. 创建集合
```python
# 直接赋值进行创建
set_val = {1, 2, 3, 4, 5, 6}
print(type(set_val))

# 创建空集合时需要注意
# 不标注set会成为元组
empty_set = ()
print(type(empty_set))
# 创建空集合时需要使用set标注
empty_set = set()
print(type(empty_set))

# 将字符串转换为集合
str_val = 'hello world'
str_to_var = set(str_val)
# 转换为无序集合，且集合的元素是不能重复的
# 利用集合可以完成自动去重的工作
print(str_to_var)

# 集合的其他特性
new_set = {'hello', 1, 3, 3.265, (1, 2, 3)}
print(new_set)
# 集合内只能包含不可变数据类型
# 列表 和 字典 是可变类型，加入集合都会报错
# new_set1 = {'hello', 1, 3, 3.265, (1, 2, 3), [1, 2, 3]}
# print(new_set1)     TypeError: unhashable type: 'list'

# 集合的特点
# 集合的元素是无序的
# 集合的元素是唯一的
# 集合自身可以被修改，但是集合中的不可变数据是不能被修改的
```

### 2. 集合的常见操作
```python
# print(dir(set))
# 1. 新增 add()
set_val = {'hello', 1, 3, (1, 3, 5)}
print(set_val)
set_val.add('world')
print(set_val)

# 2. 修改 update()
new_set = {'python'}
set_val.update(new_set)
print(set_val)

# 3. 删除
# del
# del new_set
# print(new_set)      NameError: name 'new_set' is not defined

# pop()     随机删除一个元素
# set_val.pop()
# print(set_val,)

# remove()      移除指定的元素
print(set_val)
set_val.remove('python')
print(set_val)
# 如果移除的指定元素不存在， 则会报错
# set_val.remove('inexistence')           KeyError: 'inexistence'
# print(set_val)

#discard() 移除指定元素
set_val.discard('hello')
print(set_val)
# 使用discard() 当移除的元素不存在时，不会报错，也不改变原集合
set_val.discard('inexistent')
print(set_val)

# 4. 查询
if 1 in set_val:
    print('in it')
else:
    print('not in')
```


