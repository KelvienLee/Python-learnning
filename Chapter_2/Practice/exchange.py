# 案例练习2 人命币与美元之间的互转

exchang_rate = 6.78
rmb = float(input("请输入人民币金额"))
# 用户输入的金额可能含有小数点，因此应当使用float函数，float函数既可以处理整数性数据，也可以处理浮点型数据
print('当前的汇率为', exchang_rate)
print(rmb, '元人民币', '=', rmb / exchang_rate, '美元')
