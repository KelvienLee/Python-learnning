#  求圆的面积
pi = 3.14


def area(r):
    return pi * (r ** 2)


print(area(2))

# 将分钟转换为时——分
usr_input = int(input('minutes:'))
hour = usr_input // 60
minute = usr_input % 60
print(F'{usr_input} 分钟是：')
print(F'{hour} 小时 {minute} 分钟')


def time_transform(minute1):
    hour1 = minute1 // 60
    minutes1 = minute1 % 60
    return hour1, minutes1     # 如果没有return，会返回None


print(time_transform(usr_input))            # 返回元组
# 将元组拆包
hour1, minutes1 = time_transform(180)
print(hour1)
print(minutes1)