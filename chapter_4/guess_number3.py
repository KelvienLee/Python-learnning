# 目标数字
secret_number = 8
# 最多次数
guess_limit = 3
# 已消耗次数
guessed_number = 0
# 设置标识符
# 设置标识符是其他语言通用的方法
flag = False

while guessed_number < guess_limit:
    guess = int(input("input"))
    guessed_number += 1
    if guess == secret_number:
        flag = True
        break
else:
    print('you lose')
print('game over')