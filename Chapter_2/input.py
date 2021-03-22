# Python输入函数（input）

username = input('请输入用户名')
password = input('请输入密码')
print('您输入的用户名是：',username)
print('您输入的用密码是：',password,end='\n\n')

# input输入函数默认是字符串类型，不能直接运算。
# 可使用int函数将字符串类型转换为整数型，但输入或结果也只能是整数，不能有小数点。
# 可以把int函数放在打印函数的位置
price = (input('苹果的单价是'))
number = (input('苹果数量是'))
print('苹果的总价是：',int(price)*int(number),end='\n\n')

# 也可以把int函数放在输入函数的位置
# 注意要用int函数包裹整体
price2 = int(input('香蕉的单价为：'))
number2 = int(input('香蕉的数量为：'))
print('香蕉的总价为：',price2*number2)