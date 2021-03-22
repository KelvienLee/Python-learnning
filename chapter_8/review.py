# 函数参数形式
# 1. 普通参数
print('函数的参数形式', '\n')


def say_hi(name):
    print(f'hello,{name}')


say_hi('jack')


def create_window(width, height):
    print(f'宽度：{width}  高度：{height}')


create_window(14, 7)


# 2. 默认参数
def total(hour=8, salary=30):
    print(f'今天的薪水是：{hour * salary} 元')


# 调用函数的时候，如果不定义值，就会使用默认的值，如果定义了值，就会使用定义的值。
total()
total(9)
total(8, 50)


# 3. 关键字参数
# 为了解决函数的参数顺序问题
# 可以忽略参数顺序
def student(firstname, lastname):
    print(f'first name is {firstname}  last name is {lastname}')


# 使用普通参数
student('Lucy', 'lun')
# 使用关键字参数
student(lastname='Lee', firstname='kelvin')
print()


# 4. 不定长参数
# *args 所有参数变成一个元组
# **kwargs  所有参数变成一个字典
def my_function(width, height, *args, **kwargs):
    print(args)
    print(kwargs)
    print(f'宽度是：{width} 米, 高度是：{height} 米')
    for arg in args:
        print(arg)
    for key, values in kwargs.items():
        print(f'{key} => {values}')


# 定义 **kwargs 时， 使用键值对的形式
# 如果定义了其他参数，会按顺序依次赋值给参数
my_function(15, 30, 'hello', 'world', 'this', 'is', 'a', 'test', lastname='Lee', firstname='kelvin'),
print('\n\n')

print('函数的返回值', '\n')
# 函数的返回值
# 函数执行完毕后最后得出的结果
# 求圆的面积
pi = 3.14


def area(r):
    return pi * (r ** 2)


print(area(4))


# 分钟 转换为 时——分
def transform_minute(minutes):
    hours = minutes // 60
    minute = minutes % 60
    return minutes, hours, minute


# 返回元组
print(transform_minute(100))
# 对元组进行拆包
usr_input, hours, minute = transform_minute(50)
print(f'{usr_input} 分钟可以转换为： {hours} 小时 {minute} 分钟')
print('\n\n')

# 函数的作用域
# 如果函数内部有定义的值，会先使用函数内部的值
# 如果函数内部没有定义值，回去函数外围搜寻值
# 如果在函数外围也没有找到值，就会报错
print('函数的作用域', '\n')

a = 10  # 全局变量
b = 200
l = [1, 2, 3, 4, 5]  # 这是一个可变类型的全局变量


def test1():
    a = 100  # 局部变量
    global b  # 使用 global 声名该值可以作用于全局
    b = 500
    print(b)
    print(a)
    l.append(6)  # 如果操作的变量是全局且是可变类型，不用global声名也可以作用于全局
    print(l)


def test2():
    a = 300  # 局部变量
    print(a)


print(a)
test1()
test2()
print(b)
print('\n\n')

# 函数的嵌套
print('函数的嵌套', '\n')


def test3():
    c = 10
    print('test3 开始执行')
    print(f'test3 before c = {c}')

    def test4():
        nonlocal c  # 使用 nonlocal 声明作用于外层函数
        c = 25
        print('test4 开始执行')
        print(f'test4 c = {c}')

    test4()
    print(f'test3 after c = {c}')


test3()
print('\n\n')

# 递归函数
# 递归次数太多会导致栈益处
print('函数的递归', '\n')


def fact(n):
    if n == 1:
        return 1
    result = n * fact(n - 1)
    return result


result = fact(3)
print(result)
print('\n\n')

# 匿名函数
print('匿名函数', '\n')


# lambda 表达式


def add(x, y):
    return x + y


result_5 = add(3, 4)
print(result_5)

# 格式 （ lambda 定义参数：定义操作）（赋值）
result_6 = (lambda x, y: x + y)(18, 30)
print(result_6)

# 更多操作的 lambda 格式 [（lambda 定义参数：定义操作）（赋值） 赋值操作]  使用方括号括起来
multiple = [(lambda x: x ** 2)(x) for x in range(10)]
print(multiple)
print('\n\n')


# list。sort()的使用


# 选学：函数式编程


# 函数是一等公民
print('函数是一等公民', '\n')


def func(message):
    print(f'you got a message: {message}')


# 不加括号等于传递参数，将函数赋值给他的变量名
send_message = func
send_message('hello world.')


# 如果加了括号表示调用了这个函数
send_message1 = func('this is a test.')




























