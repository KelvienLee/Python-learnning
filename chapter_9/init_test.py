class Animal(object):
    def __init__(self, name, age, hobby, food):
        """
        __init__初始化方法，在实例化对象的时候，直接调用
        """
        self.name = name
        self.age = age
        self.hobby = hobby
        self.food = food

    def information(self):
        print(f"hello, my name is {self.name}, I am {self.age} years old, my hobby is {self.hobby}.")

    def eat(self):
        print(f'I like eat {self.food} ')

    def play(self):
        print(f'{self.name} is playing')

    def sleep(self):
        # 在类中调用类的方法
        self.eat()
        print(f'After eat {self.food}, I always go to sleep.')


# 将类实例化
dog = Animal('peppa', '3', 'stepping mud', 'bread')
dog.sleep()

# 动态的为实例对象添加方法
dog.study = 'math'

print(dir(dog))

print(dog.study)













