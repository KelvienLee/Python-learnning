# dict1 = [1, 2, 3, 4, 5]
# print(dict1)
# # dict1.clear()
# # print(dict1)
# for_key = ('a', 'b', 1, 2, 3)
# new_dict = dict.fromkeys(for_key, 'hello')
# print(new_dict)
# get_val = new_dict.get('b', 1)
# print(get_val)

# dict_val = {'a': 'hello', 'b': 'world', 1: 10, 2: 20, 3: 30}
# items = dict_val.items()
# print(items)
#
# new_dict = dict_val.keys()
# print(new_dict)
# print(type(new_dict))
#
# list_dict = list(dict_val.keys())
# print(list_dict)
# print(type(list_dict))

dict_val = {'a': 'hello', 'b': 'world', 1: 10, 2: 20, 3: 30}
print(dict_val)
# dict2 = {1: 45}
# print(type(dict2))
# dict_val.update(dict2)
# print(dict_val)
#
# values = list(dict_val.values())
# print(values)
# print(type(values))
# pop_val = dict_val.pop('gjh')
# print(pop_val)
# print(dict_val)


x = True
country_counter = {}


def addone(country):
    if country in country_counter:
        country_counter[country] += 1
    else:
        country_counter[country] = 1

addone('China')
addone('Japan')
addone('china')

print(len(country_counter))

confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1] += 1

sum = 0
for k in confusion:
    sum += confusion[k]

print(sum)

