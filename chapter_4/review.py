# 复习
# i = 0
# while i <= 10:
#     print(i)
#     i += 1

# i = 1
# result_sum = 0
# while i <= 100:
#     result_sum += i
#     i += 1
# print(result_sum)

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(j, '*', i, '=', j * i, end='  ')
#         j += 1
#     print('\n')
#     i += 1

# str_val = 'hello world'
# for item in str_val:
#     print(item)

# list_val = [1, 3, 4, 5, 6, 7, 9]
# for item in list_val:
#     print(item)

# range(起始值， 结束值【不含右值】，步长)函数
# list()函数可以将range()函数内的数值强制转换为列表输出
# value = range(0, 12)
# print(list(value))
#
# for i in range(1, 11, 2):
#     print(i)
# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)

# i = 1
# sum_val = 0
# while i <= 100:
#     sum_val += i
#     i += 1
# print(sum_val)
# sum_val = 0
# for i in range(0, 101):
#     sum_val += i
# print(sum_val)

# i = 1
# j = 0
# while i <= 100:
#     j += i
#     i += 1
# print(j)

# j = 0
# for i in range(0, 101):
#     j += i
# print(j)


# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         mul = j * i
#         print(j, '*', i, '=', mul, end='  ')
#         j += 1
#     i +=1
#     print('\n')


# for i in range(1, 10):
#     for j in range(1, i + 1):
#         rel = j * i
#         print(j, '*', i, '=', rel, end='  ')
#     print('\n')

right_number = 8
guess_limit = 3
guess_used_number = 0
flag = False
while guess_used_number < guess_limit:
    guess = int(input('input:'))
    guess_used_number += 1
    if guess == right_number:
        flag = True
        break

if flag == True:
    print('you are right.')
else:
    print('you lose.')
print('game over')


# for i in range(1, 10):
#     for j in range(1, i + 1):
#         if j == 5:
#             break
#         result = j * i
#         print(j, '*', i, '=', result, end='  ')
#     print('\n')


# for i in range(1, 31):
#     if i == 4 or i == 14 or i == 18:
#         continue
#     print(i, '可以购买')

















