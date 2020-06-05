#给实例添加方法
from types import MethodType


class Student(object):
    pass


s = Student()
s.name = 'Michael'


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.name, s.age)
# 给一个实例绑定的方法，对另一个实例是不起作用的
# 可以给一个class绑定一个方法


def set_score(self, score):
    self.score = score


Student.set_score = set_score
s.set_score(89)
print(s.score)


'''
只允许对Student实例添加name和age属性。
为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，
来限制该class实例能添加的属性
'''
class Student_new(object):
    __slots__ = ('name', 'age')

s_n = Student_new()
s_n.name = 'Michael'
s_n.age = 24
s_n.score = 89 #这句执行报错“AttributeError: 'Student' object has no attribute 'score'”

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的