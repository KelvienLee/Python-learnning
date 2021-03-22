# 字典的遍历
# 遍历 key
heroes = {'及时雨': '宋江', '玉麒麟': '卢俊义', '花和尚': '鲁智深', '母夜叉': '孙二娘'}
keys = heroes.keys()
for key in keys:
    print(key)


# 遍历 value
values = heroes.values()
for value in values:
    print(value)

# 遍历 item
# 返回元组
items = heroes.items()
print(items)
for item in items:
    print(item)

# 遍历 key-value
item_val = heroes.items()
print(item_val)
for key_val, value_key in item_val:
    print(F'{key_val} => {value_key}')
