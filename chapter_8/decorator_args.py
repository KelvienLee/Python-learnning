import time
# 装饰器函数
# 带参数的函数装饰器


def my_decorator(func):
    def wrapper():
        print('wrapper start')
        start_time = time.perf_counter()
        func()
        end_time = time.perf_counter()
        print('运行时间：', end_time - start_time)
        print('wrapper end')
    return wrapper


@my_decorator
def for_loop(number):
    print('start')
    for i in range(number):
        pass
    print('end')


# new_for = my_decorator(for_loop)

# new_for()
for_loop()






