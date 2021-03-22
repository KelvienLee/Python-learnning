# print(dir(str))  # 字符串常见操作方法
# 详细使用方法可以参考帮助文档  《字符串内置方法.pdf》

# join()函数
# 将字符串连接
# list_val = ['www', 'weiguang19', 'xyz']
# str_val = '.'.join(list_val)
# print(str_val)
# tuple = ('user', 'kelvien', 'study', 'code')
# str_val= '.'.join(tuple)
# print(str_val)


# 字符串大小写转换方法 5种
# str_val = 'I love Python!'
# print(str_val.lower())                  # 全小写
# print(str_val.upper())                  # 全大写
# print(str_val.title())                  # 用于标题，即每个单词的第一个字母大写
# print(str_val.capitalize())             # 句子的第一个字母大写
# print(str_val.swapcase())               # 大小写互转

# 字符串常用检索方法
#  1. count()函数
#  区分大小写
#  str.count("被检索字符", 起始值， 结束值）   起始值和结束值可选
# words = 'i love python, this is a very interesting thing!'
# i = 'i'
# print(words.count(i, 0, 20))

#  2. find()函数
# 返回值为该子字符串的索引位置,如果未找到就返回-1
# str.find("被检索的字符串", 检索起始位置， 检索结束位置)
# j = 'v'
# print(words.find(j))

# 3. index()函数
# 用法与find()函数相似
# 如果未找到结果，会返回异常
# f = 'z'
# print(words.index(f))       # ValueError: substring not found

# 4. startswith() 函数
# 查询字符串是否以指定字符串开头
# 找到返回True，未找到返回False
# s = 'l'
# print(words.startswith(s))

# 5. endswith() 函数
# 查询字符串是否以指定字符串结尾
# 找到返回True，未找到返回False
# e = '!'
# print(words.endswith(e))


# 三种字符串的分割方法
# \t:制表符  \n:换行符  \r:回车 \r\n:回车换行
# 1. split()函数，默认使用 空格 \t, \n, \r 等进行分割
# words = 'i love python, \nthis is a very interesting thing!'        # 标点符号与前一单词相连就会合并为一个列表元素
# print(words)
# print(words.split())           # 不会输出\n
# print(words.split('i', 2))     # 以 i 为分割，分割为 num + 1 个（2 + 1 = 3） 共分成三个

# 2. splitlines()函数，默认使用 \n, \r, \r\n等进行分割
# print(words.splitlines(True))  # 默认为False， 即输出后不包含字符串格式元素。

# 3. partition()函数
# partition() 方法用来根据指定的分隔符将字符串进行分割。
# 如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。
# partition()方法语法： var.partition(str)
# str : 指定的分隔符。
# print(words.partition('o'))


# 三种字符串的修建方法
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



















