class Animal(object):
    # 定义一个类属性
    age = 6

    # 定义类方法
    def eat(self, food):
        print(f'eating {food} ')

    def play(self):
        print('playing')


# 将类实例化
dog = Animal()
dog.eat('dog food')
dog.play()
# 可以通过方法直接调用类属性
print(dog.age)

# 如果实例对象自身有该属性，会优先使用自身的属性
dog.age = 10
print(dog.age)

# 类属性自身可以直接调用
print(Animal.age)
# 同样的，类属性也可以全局动态修改
Animal.age = 15
print(Animal.age)
