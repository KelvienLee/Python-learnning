# 处理多个异常
try:
    # 异常1: 用户输入是否正确
    age = int(input('请输入年龄:'))

    # 异常2: 运算是否有错误（0不能为除数）
    x = 10 / age

# 可以把错误写到一起
except (ValueError, ZeroDivisionError):
    print('请输入整数')

# 也可以把错误分开写
# except ZeroDivisionError:
#     print('年龄不能为0')

else:
    print(f'年龄是：{age}')
    print(f'x is {x}')




















