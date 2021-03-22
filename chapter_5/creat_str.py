# 单引号创建字符串
# name = 'hello'
# hobby = "creating"
#
# zen = '''
# 给注释赋值，适合长文字的输出。
# 这是很长的一段注释
# this is a long paragraph.
# 这里面的格式          会被保留。
# '''
# print(name, hobby)
# print(zen)

# 转义字符的使用
# 这是一种错误的 is 使用方法，单引号会被识别为字符串标识符
# print('kelvien's hobby is creating things.')
# 正确的 is 使用方法是使用转义符号 \ 反斜杠 ,另外， 注意反斜杠放在前面的。解释器总是从上到下按先后顺序读取数据。
# print('kelvien\'s hobby is creating things.')
# 但是，转义符号不利于代码的阅读
# 所以，正确的使用方法应该是单引号和双引号互相 ’包裹‘
# print("kelvien's hobby is creating things.")
# print('so, what is "creating things"?')


# 索引和步长的使用
# motto = 'so, what is "creating things"?'
# love_sentence = '积善之家，必有余庆。'

# print(motto[5])                 # 通过索引取得某一个具体的值
# print(love_sentence[5:9])       # 切片同range()函数一样不包含右值
# print(love_sentence[-5:-1])
# print(love_sentence[5:])
# print(love_sentence[-5:])
# print(love_sentence[1:10:2])    # 可设置步长

# 索引越界会报错
# print(love_sentence[11])            # IndexError: string index out of range

# 切片越界会自动处理
# print('1', love_sentence[0:11])
# print('2', love_sentence[0:110])
# print('3', love_sentence[11:110])            # 返回空字符串
# print('4', love_sentence[-110:10])
# print('5', love_sentence[5:2])               # 返回空字符串
# print('6', love_sentence[-1:-10])            # 返回空字符串
# print('7', love_sentence)


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
