# 使用raise主动抛出异常
age = int(input('请输入年龄:'))


def is_adult(age):
    if age < 18:
        raise Exception("你还未成年")


try:
    is_adult(age)
except ValueError as va:
    print(va)

print('continue')
