# 创建函数
# 使用小写加下划线的形式

# def say_hi():
#     print('hello world')
#     print('welcome to weiguang19')
#
#
# say_hi()
#
#
# # 创建高楼
# def create_building():
#     print('make a room')
#     print('make a window')
#     print('make a door')


# for i in range(10):
#     create_building()


# 函数的参数
# 普通参数
# 必须为每一个参数赋值，否则会报错
# def window(width, height):
#     print(f'window width:{width} \nwindow height: {height}')
#
#
# # 普通参数按照顺序输出
# window(25, 80)
#
# # 定义参数(关键字参数）
# window(height=18, width=9)
#
#
# # 默认参数
# def total(hour, salary=20):
#     print(f'total salary of today: {hour*salary}')
#
#
# # 定义了默认参数，在使用时如果不定义对应参数，会使用默认值，如果定义了参数则使用定义的参数
# total(8)
# total(12, 10)
#
#
# # 关键字参数
# def student(firstname, lastname):
#     print(f'firstname is:{firstname}\nlastname is:{lastname}')
#
#
# student('kelvin', 'Lee')
#
#
# # 不定长参数
# def my_function(height, age, *args, **kwargs):
#     print(height)
#     print(age)
#     print(args)         # 将args输出为一个元组
#     print(kwargs)       # 将kwargs输出为一个字典
#     for arg in args:    # 遍历元组
#         print(arg)
#     for key, value in kwargs.items():       # 遍历字典
#         print(f'{key}:{value}')
#
#
# my_function(170, 18, 'hello', 'world', 'I', 'am', 'coming', lastname='kelvin', firstname='Lee')


# 函数的返回值
# 函数运行完成后返回的结果（值）
# pi = 3.14
#
#
# def area(r):
#     return pi * (r ** 2)
#
#
# print(area(2))
#
#
# # 将分钟转换为时分
# def minute_hour_exchange(input_minutes):
#     hour = input_minutes // 60
#     minute = input_minutes % 60
#     return hour, minute
#
#
# usr_input = int(input('input:'))
# print(minute_hour_exchange(usr_input))                  # 返回元组
# hours, minutes = minute_hour_exchange(usr_input)        # 将元组拆包
# print(f'{usr_input}分钟是：{hours}小时 {minutes}分钟')


# # 函数的作用域
# # 全局变量
# # 可变类型
# a = 300
# print(a)
#
# # 不可变类型
# b = [1, 2, 3]
# print(b)
#
#
# # 局部变量
# def test1():
#     a_fuc = 100
#     print(a_fuc)
#     # 对于不可变类型，需要使用global声明此操作可作用于全局
#     global a
#     a = 500
#     # 对于可变类型，不需要任何声明也能作用于全局
#     b.append(4)
#
#
# test1()
# print(a)
# print(b)


# 函数的嵌套
# def get_up():
#     print('睁开眼睛')
#     print('穿衣服')
#     print('洗脸')
#     print('刷牙')
#
#
# def breakfast():
#     print('做早餐')
#     print('吃早餐')
#
#
# # 函数的内部嵌套调用
# def to_work():
#     get_up()
#     breakfast()
#
#
# to_work()
#
#
# # 函数的内部嵌套定义编写
# def test1():
#     a = 10
#     print('test1 starts execution.')
#     print(f'test1 internal variable:{a}')
#
#     def test2():
#         nonlocal a
#         a = 100
#         print('test2 starts execution.')
#         # 内部未定义变量的值会依次向外部寻找
#         print(f'test2 internal variable:{a}')
#
#     # 提示：使用了nonlocal函数便不能再使用global函数
#     test2()
#     print('test1 starts execution.')
#     print(f'test1 internal variable:{a}')
#
#
# test1()


# 函数的递归（函数内部调用函数）
# def fact(n):
#     if n == 1:
#         return 1
#     result = n * fact(n - 1)
#     return result
#
#
# print(fact(3))

# 使用递归函数时要防止栈溢出，不要过多的使用递归次数


# 匿名函数
# 使用lambda表达式创建匿名函数

# # 普通函数形式
# def add(x, y):
#     return x + y
#
#
# result = add(5, 3)
# print(result)
#
# # lambda匿名函数形式
# expression = (lambda x, y: x + y)
# # 可直接在lambda函数后赋默认值，但是在调用时不能再赋其他的值，否则会报错
# expression2 = (lambda x, y: x + y)(10, 10)
# print(expression(5, 10))
# print(expression2)
#
# # 注意：lambda是一个表达式，并不是一个语句
# # 表达式：用一个公式去表达一个东西
# # 语句：完成了某些功能
#
# # 表达式的应用
# # 列表中使用lambda函数
# # 列表生成式
# result_apply = [x ** 2 for x in range(10)]
# print(result_apply)
#
#
# # 普通函数
# def multiple(x):
#     return x ** 2
#
#
# multiple_apply = [multiple(x) for x in range(10)]
# print(multiple_apply)
#
# # lambda表达式
# expression = [(lambda x: x ** 2)(x) for x in range(10)]
# print(expression)
#
#
# # 结合sort()函数 list.sort(key=None, reverse=False)
# # 使用函数自身特性排序
# list_value = [1, 3, 5, 64, 35, 643]
# # 从小到大排序
# list_value.sort()
# print(list_value)
# # 从大到小排序(reverse=True)
# list_value.sort(reverse=True)
# print(list_value)
#
# list_value2 = [(5, 6), (7, 3), (1, 8)]
# # 默认使用元组中的第一个元素来排序
# list_value2.sort()
# print(list_value2)
# list_value2.sort(reverse=True)
# print(list_value2)
#
#
# # 使用key定义如何排序
# # 使用函数来定义排序规则
# def second_num(list_val):
#     return list_val[1]
#
#
# list_value2.sort(key=second_num)
# print(list_value2)
#
# list_value2.sort(key=second_num, reverse=True)
# print(list_value2)
#
# # 使用lambda函数定义排序规则
# list_value2.sort(key=lambda x: x[1])
# print(list_value2)
# list_value2.sort(key=lambda x: x[1], reverse=True)
# print(list_value2)
#
#
# # 匿名函数的作用
# # 简化代码、提高可读性


# 函数是一等公民
# 可以赋值
# def func(message):
#     print(f'You got a message:{message}')
#
#
# # 将函数赋值给其他变量
# # 注意将函数对象赋值给其他变量的时候<!没有括号>,如果有括号则表示<!输出一个结果了>
# send_message = func
# # 赋值之后就可以在这个变量中为定义的函数传递参数
# send_message('hello world')
#
#
# # 可以作为参数
# def get_message(message):
#     return f'You got a message:{message}'
#
#
# def call(fun, message):
#     print(fun(message))
#
#
# call(fun=get_message, message='hello,world')
# call(get_message, 'hello,world')
#
#
# # 可以嵌套
# def fun_3(message):
#
#     def get_message_3(message_3):
#         print(f'You got a message:{message_3}')
#     return get_message_3(message)
#
#
# fun_3('hello world')
#
#
# # 可以作为返回值
# def func_4():
#
#     def get_message_4(message):
#         return f'You got a message:{message}'
#     # 返回这个函数,而不是返回函数的值
#     # get_message_4()这个函数作为一个值被返回出去了
#     return get_message_4
#
#
# # 调用func_4()这个函数得到的值就是一个返回值,即调用了send_message_4()这个函数
# send_message_4 = func_4()           # send_message_4 = get_message_4
# message_string = send_message_4('hello world')            # get_message()
# print(message_string)


# 函数装饰器
# import time
#
#
# # 定义一个普通函数,用于计算程序运行时间
# def my_decorator(func):
#     def wrapper():
#         print('wrapper starting')
#         start_time_wrapper = time.perf_counter()
#         func()
#         end_time_wrapper = time.perf_counter()
#         result_time_wrapper = end_time_wrapper - start_time_wrapper
#         print(f'wrapper running time:{result_time_wrapper}')
#         print('wrapper end')
#     return wrapper
#
#
# # 使用函数装饰
# @my_decorator
# def for_loop():
#     print('for_loop starting')
#     for i in range(100000):
#         pass
#     print('for_loop end')
#
#
# # 使用函数装饰器
# @my_decorator
# def while_loop():
#     print('while_loop starting')
#     i = 0
#     while i < 100000:
#         i += 1
#     print('while_loop end')

# 使用普通方法计算程序运行时间 (time.perf_counter()函数加减得出)
# start_time = time.perf_counter()
# for_loop()
# end_time = time.perf_counter()
# result_time = end_time - start_time
# print(result_time)


# 普通方法调用函数计算程序运行时间
# new_for = my_decorator(for_loop)        # wrapper()
# new_for()
#
# new_while = my_decorator(while_loop)
# new_while()

# 使用了函数装饰器后,调用函数时直接包含了装饰器函数的功能
# for_loop()
# while_loop()
#
# print('\n\n')


# 带参数的函数装饰器
# def time_counter(func):
#     def time_wrapper(number):
#         print('wrapper function starting')
#         func_start_time = time.perf_counter()
#         func(number)
#         func_end_time = time.perf_counter()
#         result = func_end_time - func_start_time
#         print(f'wrapper running time:{result}')
#         print('wrapper function end')
#     return time_wrapper
#
#
# @time_counter
# def for_loop_wrapper(number):
#     print('for_loop_wrapper starting')
#     for i in range(number):
#         pass
#     print('for_loop_wrapper end')
#
#
# for_loop_wrapper(10000000)


# 带有可变参数的函数装饰器
import functools


# def time_counter(func):
#     # 使用functools.wraps()函数来保存原函数的元信息
#     @functools.wraps(func)
#     def time_wrapper(*args, **kwargs):
#         print('wrapper function starting')
#         func_start_time = time.perf_counter()
#         func(*args, **kwargs)
#         func_end_time = time.perf_counter()
#         result = func_end_time - func_start_time
#         print(f'wrapper running time:{result}')
#         print('wrapper function end')
#     return time_wrapper
#
#
# @time_counter
# def welcome(*args, **kwargs):
#     name, gender = args
#     gender = '男士' if gender == '男' else '女士'
#     print(f'hello,{name}{gender}, you are {kwargs["age"]} years old, your hobby is {kwargs["hobby"]}')
#
#
# welcome('kelvin', '男', age='18', hobby='football')
#
# # 打印函数的元名称
# print(welcome.__name__)

def decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper1 function execution')
        func(*args, **kwargs)
    return wrapper


def decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper2 function execution')
        func(*args, **kwargs)
    return wrapper


@decorator1
@decorator2
def welcome(message):
    print(message)


welcome('hello world')
