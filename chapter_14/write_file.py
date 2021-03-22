# 打开文件
file = open('test.txt', 'w', encoding='utf-8')

# 写入文件
# 写入字符串(write)
# file.write('hello \nworld')

# 写入字符串序列(writelines)
seq = ['人生苦短', '我用Python', 'hello', 'world']
file.writelines('\n'.join(seq))                     # 自动换行效果

# 关闭文件
file.close()
