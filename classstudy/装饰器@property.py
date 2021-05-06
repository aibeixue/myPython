#通过多重继承可以解决子类继承父类层级过多的问题，
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能

#动物父类
class Animal:
    pass
#哺乳类东西
class Mammal(Animal):
    pass
#鸟类动物
class Bird(Animal):
    pass


class Runnable:
    def run(self):
        print('runing.....')
class Flyable:
    def fly(self):
        print('flying.....')

class Dog(Mammal,Runnable):
    pass

class Bat(Mammal,Runnable):
    pass

class Parrot(Bird,Flyable):
    pass

class Ostrich(Bird,Flyable):
    pass

dog=Dog()
dog.run()

parrot=Parrot()
parrot.fly()