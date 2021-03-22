# 比较运算符
# a = 5
# b = 6
# c = 5
# print(a < b)
# print(a > b)
# print(a >= c)
# print(a != c)
# print(a != b)

# 比较运算符的运用
print('成绩判断', end='\n\n')
scoreNub = float(input('请输入你的成绩: '))
score = scoreNub
if score >= 60:
    print('成绩及格', end='\n\n')
else:
    print('成绩不及格', end='\n\n')

print('猜数字小游戏', '\n')
deNub = 6
inNub = int(input('请输入数字： '))
if deNub == inNub:
    print('答对了，不错啊小伙子')
else:
    print('答错了')
