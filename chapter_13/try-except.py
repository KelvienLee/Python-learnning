# 异常处理

# 使用 try...except处理异常
# 程序正常，执行try范围内的程序
try:
    age = int(input('请输入年龄：'))
    if age >= 18:
        print('你已成年')
    else:
        print('你未成年')

# 如果出现异常，执行except语句内的程序
except ValueError as error:
    print('输入不合法')
    print(error)

print('程序结束')


# 使用try...except...else 处理异常




















