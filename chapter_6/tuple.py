# 创建元组
tuple_val = (1, 'hello', [1, 2, 31], (4, 65, 757, 67))
empty_tuple = tuple()

# 这样创建只有一个元素的元组会变成对应类型
tuple_0 = ('hello')
print(type(tuple_0))
tuple_1 = (1)
print(type(tuple_1))

# 如果需要将只有一个元素的“元组”转换为元组，需要在其后面添加一个逗号 ,
tuple_0 = ('hello',)
print(type(tuple_0))
tuple_1 = (1,)
print(type(tuple_1))


# 在元组中使用索引和切片
# 索引
print(tuple_val[1])
print(tuple_val[2])
# 切片
print(tuple_val[-1][1:3])

# 遍历
for i in tuple_val:
    print(i)

# 不可变类型
# tuple_val[0] = 2        ypeError: 'tuple' object does not support item assignment

# 常见操作
print(dir(tuple))
my_tuple = tuple_val = (1, 'hello', [1, 2, 31], (4, 65, 757, 67), 1)
print(my_tuple.count(1))
print(my_tuple.index(1))

# 元组拆包
info = ('kelvien', 'lee', 22, [1, 2, 3])
first_name, last_name, age, others = ('kelvien', 'lee', 22, [1, 2, 3])
print(first_name)
print(last_name)
print(age)
print(others)

# 使用占位符 (下划线 _) 拆包
_, _, age_new, _ = ('kelvien', 'lee', 22, [1, 2, 3])
print(age_new)

# 元素较多
# *rest 会省去中间所有内容
a, b, *rest, c, d = range(1, 11)
print(a)
print(b)
print(c)
print(d)
print(*rest)

# 快速交换
number1 = 1
number2 = 2
number1, number2 = number2, number1
print(number1)
print(number2)











