# 1. 用两种方法判断奇偶数

# method 1
# uin = int(input('input:'))
# if uin % 2 == 0:
#     print('even number')
# else:
#     print('odd number')

# method 2
# uin = int(input('input:'))
# output = 'even number' if uib % 2 == 0 else 'odd number'
# print(output)

# 2. 电梯设置 不能超过10人 且 不能超过 1000千克
# number_of_people = int(input('people:'))
# weight = int(input('weight:'))
# if number_of_people <= 10 and weight <= 1000:
#     print('here we go!')
# else:
#     print('oh,the last people should go out.')


# 根据年龄输出人生阶段
# uin = int(input('input:'))
# if 0 <= uin <= 6:
#     age = '童年'
# elif 7 <= uin <= 17:
#     age = '少年'
# elif 18 <= uin <= 40:
#     age = '青年'
# elif 41 <= uin <= 65:
#     age = '中年'
# elif uin > 65:
#     age = '老年'
# else:
#     age = '你还在娘胎里'
# print(age)
#
#


# 石头剪刀布随机生成游戏
# 代码可优化
# import random
# uin = int(input('剪刀 0，石头 1，布 2, 请输入： '))
# ran_gnr = random.randint(0, 2)
# if uin == 0 and ran_gnr == 1:
#     result = 'you lose'
# elif uin == 0 and ran_gnr == 2:
#     result = 'you win'
# elif uin == 1 and ran_gnr == 0:
#     result = 'you win'
# elif uin == 1 and ran_gnr == 2:
#     result = 'you lose'
# elif uin == 2 and ran_gnr == 0:
#     result = 'you lose'
# elif uin == 2 and ran_gnr == 1:
#     result = 'you win'
# else:
#     result = 'draw'
#
# if uin == 0:
#     icon = '剪刀'
# elif uin == 1:
#     icon = '石头'
# elif uin == 2:
#     icon = '布'
#
# if ran_gnr == 0:
#     icon1 = '剪刀'
# elif ran_gnr == 1:
#     icon1 = '石头'
# elif ran_gnr == 2:
#     icon1 = '布'
#
# print('你出的是：', uin, icon)
# print('电脑出的是：', ran_gnr, icon1)
# print('比赛结果是:', result)











