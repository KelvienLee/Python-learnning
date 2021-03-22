# 打开文件
file = open('test.txt', 'w')

# 写入文件
file.write('人生苦短，我用Python。')
# 如果要换行，可使用\n
file.write('人生苦短，\n我用Python。')

# 字符串序列可使用列表或元组
sep = ['人生苦短', '我用Python。']
# 默认紧密拼接字符，不会自动换行
file.writelines(sep)
# 如果想要实现自动换行的效果，可使用字符串join()方法
file.writelines('\n'.join(sep))

# 关闭文件
file.close()
