# 操作文件指针的常用方法

file = open('zen.txt', 'w+')
print(file.tell())
file.write('人生苦短，我用Python.')

# 将文件指针调到起始位置
file.seek(0, 0)

print(file.tell())
content = file.read()
print(content)

file.close()
