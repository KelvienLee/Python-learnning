class Animal(object):
    def eat(self, food):
        print(f'eating{food} ')

    def play(self):
        print('playing')

    def sleep(self):
        print('sleeping')


dog = Animal()
dog.eat('dog food')
dog.play()
dog.sleep()
