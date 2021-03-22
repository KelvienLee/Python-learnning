# 使用 try...except...else处理异常
try:                                      # 判断条件
    age = int(input('请输入年龄：'))

# 如果程序异常，执行except语句内的操作
except ValueError as error:
    print('输入不合法')

# 如果程序正常，执行else语句内的操作
else:
    if age >= 18:
        print('你已成年')
    else:
        print('你未成年')

print('程序结束')
