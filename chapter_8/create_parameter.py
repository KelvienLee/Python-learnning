# 函数的参数形式
# 1. 普通参数
# 省去关键字参数定义的时候，一定要按固定顺序
# 函数必须一一对应赋值，不然会出现错误
def say_hello(name, level):
    print('hello')
    print(F'{name}')
    print(F'您是VIP{level}会员')


say_hello(name='jack', level=8)
say_hello('jack', 8)


# 2. 默认参数
# 如果定义了默认参数，使用时未定义参数，就是使用默认参数
# 如果使用时定义了参数，就会使用定义后的参数
def total(hour, salary=10):
    print(F'您今天的薪水是：{hour * salary} 元')


total(8)
total(8, 20)


# 3. 关键字参数
# 使用关键字参数时顺序可以不固定
def student(firstname, lastname):
    print(f'firstname is: {firstname}, lastname is: {lastname}')


student('kelvin', 'lee')
student(lastname='lee', firstname='kelvin')
print('\n')


# 4. 不定长参数
# argument 参数
# *args 相当于一个容器
# 使用了关键字参数会转为字典对应输出
# 一个 * 号表示一个元组
# 两个 * 号表示一个字典
def my_function(width, height, *args, **kwargs):
    print(width)
    print(height)
    print(args)             # 这是一个元组
    print(kwargs)           # 这是一个字典
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f'{key} => {value}')


# 参数会依次传递
my_function(12.5, 8.5, 'hello', 'world', 1 + 2, [1, 2, 3], name='kelvin', age=22)


































