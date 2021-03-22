# 类的继承

class Animal(object):
    age = 10

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating.')

    def play(self):
        print(f'{self.name} is playing.')

    def sleep(self):
        print(f'{self.name} is sleeping')


class Pig(Animal):
    # 子类可以继承父类的实例属性
    def food(self):
        print(f'Pig {self.name} like pig food.')


class Dog(Animal):
    def food(self):
        print(f'Dog like dog food.')


# 调用子类必须添加父类要求的必要属性
dog = Dog('Labrador')
print(dog)
# 子类可以调用父类的实例方法
dog.eat()
print(dog.age)


















