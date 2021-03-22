# 测试字符串
# 空字符串 "" ''
# if '':                      # '' = False
#     print('这是True')
# else:
#     print('这是False')

# 整型 0: False
# if 0:
#     print('True')
# else:
#     print('False')

# List/Tuple/Dict/Set
if ['']:                    # 列表内只要有元素就为真
    print('True')
else:
    print('False')


if (1):                      # 元组内只要有元素就为真
        print('True')
else:
        print('False')

if {2}:                      # 元组内只要有元素就为真
        print('True')
else:
        print('False')

if set():                   # 集合内只要有元素就为真
        print('True')
else:
        print('False')

# 对象类型 Object
if None:                     # 对象类型，None 为False,其余的都为True
    print('True')
else:
    print('False')
