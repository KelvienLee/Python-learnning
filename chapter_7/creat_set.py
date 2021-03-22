# 创建集合
# 直接赋值进行创建
set_val = {1, 2, 3, 4, 5, 6}
print(type(set_val))

# 创建空集合时需要注意
# 不标注set会成为元组
empty_set = ()
print(type(empty_set))
# 创建空集合时需要使用set标注
empty_set = set()
print(type(empty_set))

# 将字符串转换为集合
str_val = 'hello world'
str_to_var = set(str_val)
# 转换为无序集合，且集合的元素是不能重复的
# 利用集合可以完成自动去重的工作
print(str_to_var)

# 集合的其他特性
new_set = {'hello', 1, 3, 3.265, (1, 2, 3)}
print(new_set)
# 集合内只能包含不可变数据类型
# 列表 和 字典 是可变类型，加入集合都会报错
# new_set1 = {'hello', 1, 3, 3.265, (1, 2, 3), [1, 2, 3]}
# print(new_set1)     TypeError: unhashable type: 'list'

# 集合的特点
# 集合的元素是无序的
# 集合的元素是唯一的
# 集合自身可以被修改，但是集合中的不可变数据是不能被修改的

























