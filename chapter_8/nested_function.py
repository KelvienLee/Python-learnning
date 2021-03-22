def test1():
    print('hello')
    a = 100
    print(a)

    def test2():
        print('world')
        # a = 10            # 未在函数内部定义变量，会去函数外层寻找变量
        print(a)
    test2()


test1()


def test3():
    c = 5
    print(c)

    def teat4():
        nonlocal c              # 在函数内部嵌套函数时，要改变外层变量的值使用nonlocal()函数
        c = 18
        print(c)
    teat4()


test3()





















