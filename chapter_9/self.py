class Animal(object):
    def eat(self, food):
        print(f'eating {food} ')

    def play(self):
        print('playing')

    def sleep(self):
        # 在类中调用类的方法
        self.eat('some food')
        print('sleeping')


# 将类实例化
dog = Animal()
dog.eat('dog food')
dog.play()
dog.sleep()

# 可以使用类名直接调用（将类直接实例化）
# 但是这种方法需要主动传播self元素才能使用，不如使用将类赋值实例化的方法
# 因此并不提倡这种实例化方法
Animal()
Animal.eat(dog, 'dog milk')
Animal.sleep(dog)
Animal.play(dog)





