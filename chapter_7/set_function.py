# 集合的常见操作
# print(dir(set))
# 1. 新增 add()
set_val = {'hello', 1, 3, (1, 3, 5)}
print(set_val)
set_val.add('world')
print(set_val)

# 2. 修改 update()
new_set = {'python'}
set_val.update(new_set)
print(set_val)

# 3. 删除
# del
# del new_set
# print(new_set)      NameError: name 'new_set' is not defined

# pop()     随机删除一个元素
# set_val.pop()
# print(set_val,)

# remove()      移除指定的元素
print(set_val)
set_val.remove('python')
print(set_val)
# 如果移除的指定元素不存在， 则会报错
# set_val.remove('inexistence')           KeyError: 'inexistence'
# print(set_val)

#discard() 移除指定元素
set_val.discard('hello')
print(set_val)
# 使用discard() 当移除的元素不存在时，不会报错，也不改变原集合
set_val.discard('inexistent')
print(set_val)

# 4. 查询
if 1 in set_val:
    print('in it')
else:
    print('not in')
