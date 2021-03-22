print('this is package2 module3')

# 使用__all__声明只能调用那些方法
# 未被声明的方法将不能被调用
__all__ = ['add', 'subtraction', 'multiplication', 'division']


def add():
    print('this is add_function')


def subtraction():
    print('this is subtraction function')


def multiplication():
    print('this is multiplication')


def division():
    print('this is division')


def test():
    print('this is a test.')