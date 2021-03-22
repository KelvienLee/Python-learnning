# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(j, '*', i, '=', j * i, end='  ')
#         j += 1
#     i += 1
#     print('\n')

for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, '*', i, '=', j * i, end='  ')
    print('\n')
