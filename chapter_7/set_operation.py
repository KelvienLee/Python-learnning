# 集合的常见运算operation

# 1. 交集 intersection()
set1 = {1, 2, 3, 30, 40, 50}
set2 = {30, 40, 50, 60, 70, 80}
print(set1)
print(set2)
intersection = set1.intersection(set2)
# 不会影响原来的集合，返回新的集合
print(intersection)

intersection_update = set1.intersection_update(set2)
# 将集合1更新为运算后的交集，返回 None
print(set1)
print(intersection_update)

# 2. 并集 union()
# 不会影响原来的集合，返回新的集合
set3 = {1, 2, 3, 30, 40, 50}
set4 = {30, 40, 50, 60, 70, 80}
union = set3.union(set4)
print(union)


# 3. 差集 difference()
set3 = {1, 2, 3, 30, 40, 50}
set4 = {30, 40, 50, 60, 70, 80}
# 去除本集合中与参数集合相同的元素，返回新的集合
# 不改变原来的集合
difference = set3.difference(set4)
print(set3)
print(set4)
print(difference)

# difference_update()
intersection_update = set3.difference_update(set4)
print(set3)
print(set4)
print(intersection_update)
























