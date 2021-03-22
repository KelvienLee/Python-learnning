# 目标数字
secret_number = 8
# 最多次数
guess_limit = 3
# 已消耗次数
guessed_number = 0

while guessed_number < guess_limit:
    guess = int(input("input"))
    guessed_number += 1
    if guess == secret_number:
        print('you wing')
        break

print('game over')