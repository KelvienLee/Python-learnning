# 判断奇偶数
# inp_num = int(input('input:'))
# if inp_num % 2 == 0:
#     print('this is even number')
# else:
#     print('this is odd number')

# 判断是否要加班然后觉得是否要去看电影
# if else 都要使用
# work_overtime = True
# if work_overtime:
#     print('go home')
# else:
#     print('go movie then')
#     print('go home')

# 巧用 if not, 可以只使用if 而达到目的
# work_overtime = True
# if not work_overtime:
#     print('go movie then')
#
# print('go home sleep')

# 根据天气发出对应提醒
# is_hot = True
# if is_hot:
#     print('today is hot, you need drink more.')
# else:
#     print('today is not hot, enjoy it.')
# print('have a good day!')

# is_hot = False
# if is_hot:
#     print('today is hot, drink water more.')
# else:
#     print('today is cold, wear more.')
#
# print('have a good day.')
#
# is_hot = False
# if is_hot:
#     print('today is hot, drink water more.')
#
# print('have a good day.')


# is_hot = False
# is_cold = False
# is_windy = False
# is_foggy = True
#
# if is_hot:
#     print('it is hot today.')
# elif is_cold:
#     print('it is cold today.')
# elif is_windy:
#     print('it is windy today.')
# elif is_foggy:
#     print('it is fog today.')
# else:
#     print('have a good day!')

# usr_nub_len = input('input your username')
# if len(usr_nub_len) < 3:
#     print('user name requires at least 3 characters.')
# elif len(usr_nub_len) > 50:
#     print('user name cannot exceed 50 characters.')
# else:
#     print('username is valid')


# has_house = False
# has_car = False
# low_level = 0
# if not low_level:
#     if has_car and has_house:
#         print('you are very good!')
#     elif has_car or has_house:
#         print('you are good!')
#     else:
#         print('you just so so.')
# else:
#     print('no, you can not.')


# 三元运算符/ 三目运算符
# x = 52
# y = - x if x <= 0 else x
# print(y)

# x = 0
# if x >= 0:
#     y = x
#     print(y)
# else:
#     y = - x
#     print(y)

# a = 58
# b = 85
# c = a if a >= b else b
# print(c)
# if a >= b:
#     c = a
# else:
#     c = b
# print(c)


# 省略喷段条件

import random

user_input_number = int(input('input'))
right_number = random.randint(0, 9)
if user_input_number == right_number:
    print('you are right!')
else:
    print('you are wrong!')
    print('the right number is:', right_number)












