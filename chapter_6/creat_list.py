# 直接给列表赋值
'''
food_list = ['方便面', '酸奶', '雪糕', '方便面', 12, 45.86, [1, 3, 'hello']]
# 检测数据类型的两种方法：
print(type(food_list))
print(isinstance(food_list, list))          # 预测是否为列表类型，如果是，返回True，否则返回False

# 创建空列表
list1 = []
print(type(list1))
list2 = list()
print(type(list2))
str_val = 'hello'
list3 = list(str_val)
print(list3)
'''
food_list = ['方便面', '酸奶', '雪糕', '方便面', 12, 45.86, [1, 3, 'hello']]
# print(food_list[6])
# print(food_list[-1])
print(food_list[-1][1:3])
print(food_list[6][0:2])
























































