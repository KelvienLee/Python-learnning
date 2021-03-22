# 列表最简形式
list_val = []
for i in range(0, 6):
    list_val.append(i ** 2)

print(list_val)

# 列表推导式
new_list = [i ** 2 for i in range(0, 6)]
print(new_list)

word_list = ['hello', 'world', 'I', 'love', 'Python']
new_list_again = [i.upper() for i in word_list]
print(new_list_again)

# 列表推导式 包含过滤条件
# 普通方法
list_val_filter = []
for i in range(21):
    if i % 2 == 0:
        list_val_filter.append(i)
print(list_val_filter)

# 列表推导式喊过滤最简形式
new_list2 = [j for j in range(21) if j % 2 == 0]
print(new_list2)

the_new_names = ['hello', 'world', 'i', 'am', 'coming']
the_list_val = []
for s in the_new_names:
    if len(s) < 3:
        the_list_val.append(s.lower())
    else:
        the_list_val.append(s.upper())
print(the_list_val)

the_new_new_files = [s.lower() if len(s) < 3 else s.upper() for s in the_new_names]
print(the_new_new_files)

# 列表推导式 循环嵌套形式
# for 循环嵌套
for_list = []
for k in '高富帅':
    for h in '白富美':
        for_list.append(k + h)
print(for_list)

the_last_list = [k + h for k in '高富帅' for h in '白富美']
print(the_last_list)































