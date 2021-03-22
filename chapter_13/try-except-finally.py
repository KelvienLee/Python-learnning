# 使用try...except...finally 处理异常

try:
    file = open('text.txt', 'w')
    s = 'hello world2.'
    file.write(s)

except:
    print('操作异常')

# 无论是否发生异常，都要执行的操作
finally:
    file.close()
    print('关闭文件')
