# 打开文件
file = open('test.txt', 'r', encoding='utf-8')

# 操作文件
# read()方法
content = file.read()
print(content)


# readline()方法
# 一般不会使用这种方法：
line = file.readline()
print(line)             # hello\n
line = file.readline()
print(line)
line = file.readline()
print(line)
line = file.readline()
print(f'结束：{line}')

# 使用while语句依次读取：
line = file.readline()
while line != '':
    print(line, end='')
    line = file.readline()


# readlines()方法
# 返回列表
lines = file.readlines()
print(lines)

for line in lines:
    print(line, end='')

# 关闭文件
file.close()
