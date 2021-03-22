# for i in range(1, 10):
#     for j in range(1, i + 1):
#         # print(j, '*', i, '=', j * i, end='  ')
#         print(F'{j} * {i} = {j * i}', end='  ')
#     print('\n')

# 只要使用了f-string, {}大括号内就不能出现转义符号 \ ，否则就会报错
# import random
# val_nub = random.randint(0, 10)
# user_input = int(input('input:'))
# if val_nub == user_input:
#     print('you are right.')
# else:
#     print('the right numver is:', val_nub)
#     print('you lose.')
# print('game over.')
