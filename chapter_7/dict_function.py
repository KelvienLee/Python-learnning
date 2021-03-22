# 字典的常见操作
# 1. 新增数据
heroes = {'及时雨': '宋江', '玉麒麟': '卢俊义', '花和尚': '鲁智深', '母夜叉': '孙二娘'}
heroes['豹子头'] = '林冲'
print(heroes)

# 2. 修改数据
heroes['及时雨'] = '宋公明'
print(heroes)

# update() 将新的字典的值添加到另一字典当中
# 如果新的字典里有值与既定字典的值相同，则不会添加进去
# 如果新字典的值发生改变，则会覆盖既定字典的值
more_heroes = {'黑旋风': '李逵', '入云龙': '公孙胜'}
heroes.update(more_heroes)
print(heroes)

# 3. 删除操作
# del()
# 删除一个元素
del heroes['及时雨']
print(heroes)
# 删除整个字典
# del heroes
# print(heroes)   NameError: name 'heroes' is not defined

# pop()     根据键名删除指定元素
heroes.pop('花和尚')
print(heroes)
# 如果键名不存在则会出现错误
# heroes.pop('麒麟')
# print(heroes)   KeyError: '麒麟'

# popitem() 删除最后一个元素
heroes.popitem()
print(heroes)

# clear() 删除整个字典的所有元素，并保留空字典
# heroes.clear()
# print(heroes)


# 4. 查询列表
# 根据键名进行查询
if '豹子头' in heroes:
    print('in')
else:
    print('not in')

# 5. 字典取值
# key()
# 取出键名
keys = heroes.keys()
print(keys)
print(list(keys))
for key in keys:
    print(key)

# values()
# 取出键值
hero_val = heroes.values()
print(hero_val)
print(list(hero_val))
for val_key in hero_val:
    print(val_key)

# items()
items = heroes.items()
print(items)
print(list(items))
print(list(items)[0])
# 利用元组拆包拆分字典
t_key, t_value = list(items)[0]
print(t_key)
print(t_value)
# for item_val in items:
#     print(item_val)

# 6. 字典复制
# copy()
# 字典是可变类型 可使用copy()函数保存副本
heroes_copy = heroes.copy()
