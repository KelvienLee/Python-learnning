# 类的继承

class Animal(object):

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating.')

    def play(self):
        print(f'{self.name} is playing.')

    def sleep(self):
        print(f'{self.name} is sleeping')


class Pig(Animal):

    def __init__(self, name, gender):
        # 子类的初始化方法会覆盖父类的初始化方法
        # 如果要在子类中调用父类的初始化方法，需要调用super()方法进行声明
        # 需要接受什么参数，就调用什么参数
        super().__init__(name)
        self.gender = gender

    def food(self):
        print(f'Pig {self.name} like pig food.')


pig = Pig('pep', 'girl')
# 成功调用了父类的初始化方法
pig.food()

