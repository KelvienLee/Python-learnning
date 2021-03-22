a = 100


def test1():
    b = 300
    print(b)


def test2():
    b = 300
    # b = 200
    print(b)
    # print(b)


test1()
test2()
# 在函数中定义的变量只有在函数中才能输出（局部变量）
# print(b)            # NameError: name 'b' is not defined
print(a)              # 全局变量，可以正常输出


# 使用global()函数在函数内操作全局变量
def test3():
    global a
    a = 500
    print(a)


test3()
print(a)

# 对于一个全局变量，如果他是一个可变类型，那么不用global()函数也可以在函数内对其数值进行修改
c = [1, 2, 3]


def test3():
    c.append(4)
    print(c)


test3()






















