# 实例练习 猜数字小游戏

import random                                   # 引入随机模块

inp_num = int(input('请输入0到9之间的数字'))
rig_num = random.randint(0, 9)                  # 定义随机数值为整型，随机范围为 0 - 9
if inp_num == rig_num:
    print('you are right!')
else:
    print('you are wrong!')
    print('正确答案是：', rig_num)
