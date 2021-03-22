# 创建字典
# 字典没有索引和切片
heroes = {'及时雨': '宋江', '玉麒麟': '卢俊义', '花和尚': '鲁智深', '母夜叉': '孙二娘'}
print(type(heroes))

empty_dict = dict()
print(type(empty_dict))

hero_star = {'天罡星': {'及时雨': '宋江', '玉麒麟': '卢俊义'},
             '地煞星': {'花和尚': '鲁智深'}}

print(heroes['花和尚'])
print(hero_star['天罡星']['玉麒麟'])
print(hero_star['天罡星']['及时雨'])

# 如果键名相同，会默认取最后一个值
# 所以一个字典中不要使用相同的键名
dict_val = {'黑旋风': '李逵', '黑旋风': '李鬼'}
print(dict_val['黑旋风'])

# 键值可以相同
dict_val2 = {'及时雨': '宋江', '呼保义':'宋江', '忠义黑三郎': '宋江'}
print(dict_val2['及时雨'])
print(dict_val2['呼保义'])
print(dict_val2['忠义黑三郎'])
