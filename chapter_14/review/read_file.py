# 打开文件
file = open('test.txt', 'r')

# 操作文件
content = file.read()               # 读取所有内容
line = file.readline()              # 读取第一行

# 遍历所有行
for line in file:
    print(line, end='')

lines = file.readlines()            # 返回列表
# 遍历内容列表
for line in lines:
    # 可使用end为空去除空行
    print(line, end='')

# 关闭文件
file.close()
