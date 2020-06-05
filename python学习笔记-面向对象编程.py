'''
在OOP程序设计中，当我们定义一个class的时候，
可以从某个现有的class继承，新的class称为子类（Subclass），
而被继承的class称为基类、父类或超类（Base class、Super class）
'''
import types


class Animal(object):
    def run(self):
        print('Animal is running...')

'''
继承有什么好处？最大的好处是子类获得了父类的全部功能。
由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，
就自动拥有了run()方法
'''


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')

    def eat(self):
        print('Eating fish...')


dog = Dog()
dog.run()
cat = Cat()
cat.run()

'''
多态：子类可对继承自父类的方法进行重写，调用时，
子类实例调用子类重写后的方法，父类实例调用父类原有的方法
对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，
就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象
上，由运行时该对象的确切类型决定，这就是多态真正的威力
'''


class Timer(object):
    def run(self):
        print('Start...')

'''
动态语言的“鸭子类型”：并不要求严格的继承体系，
一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子

run_twice(Animal) 对传入的对象不做强制要求是继承自Animal，只要传入的对象有run方法就行
'''


#配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：


'''
getattr():获取对象属性
setattr():设置对象属性
hasattr():判断是否有该属性
'''


def run_twice(Animal):
    Animal.run()
    Animal.run()


run_twice(Timer())
print(type(run_twice) == types.FunctionType)
print(dir(Animal))

# getattr（obj,'z',404） 如果属性‘Z’不存在则返回默认值404。