import json

# 字典转化为json格式
# dict_value = {'name': 'kelvin', 'age': 19, 'hobby': ['basketball, football, baseball']}
# print(dict_value)
# print(type(dict_value))
# json_str = json.dumps(dict_value)
# print(json_str)
# print(type(json_str))


# 存储到文件中
# file = open('json.txt', 'w')
# json.dump(dict_value, file)

file_open = open('json.txt', 'r')
open_result = json.load(file_open)
print(open_result)
# 将json转化为字典
# json_transform = json.loads(json_str)
# print(json_transform)
# print(type(json_transform))
