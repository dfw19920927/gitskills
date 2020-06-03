from functools import reduce
import time


'''
map()函数，接收两个参数，一个是函数，一个是Iterable（可迭代对象），
map将传入的函数依次作用到序列的每个元素，并把结果作为一个行的Iterable返回
'''

def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6,7])
list(r)
#输出1,4,9...49

list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
#输出：['1', '2', '3', '4', '5', '6', '7', '8', '9']


"""
reduce()函数，把一个函数作用到一个序列[x1,x2,x3...xn]上，这个函数必须接受两个参数
reduce把结果继续和序列的下一个元素做累积计算
"""

reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)


#练习：将字符数据转换为int值
DIGITS={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

#练习2：将字符数据转换为float值
def str2float(s):
    s_split = s.split('.')

    def fn1(x,y):
        return x*10+y

    def fn2(x, y):
        return x/10+y

    def char2num(str):
        return DIGITS[str]

    s1 = reduce(fn1, map(char2num, s_split[0]))
    s2 = reduce(fn2, map(char2num, s_split[1]))[::-1]/10
    return s1+s2

#返回函数:将函数作为结果值返回
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax+=n
        return ax
    return sum
'''
>>> f = lazy_sum(1, 3, 5, 7, 9)
>>> f
<function lazy_sum.<locals>.sum at 0x101c6ed90>
>>> f()
25
'''
#闭包:们在函数lazy_sum中又定义了函数sum，并且，
# 内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，
# 相关参数和变量都保存在返回的函数中
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
'''
>>> f1()
9
>>> f2()
9
>>> f3()
9
全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9

返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量
'''
#练习
def createCounter():
    ax = []
    def count():
        ax[0] = ax[0] + 1
        return ax[0]
    return count()

#匿名函数 lambda 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
f = lambda x:x*x


#装饰器：要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，
# 称之为“装饰器”（Decorator）

def now():
    print('2020-06-01')

#借助Python的@语法，把decorator置于函数的定义处
def log(func):
    def wrapper(*args,**kw):
        print('call %s():',%func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def new_now():
    print('2020-06-02')

'''
>>> now()
call now():
2015-3-25
把@log放到now()函数的定义处，相当于执行了语句：now = log(now)
由于log()是一个decorator，返回一个函数，
所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数
'''

#如果decorator本身需要传入参数，
# 那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

def log_text(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

#高阶decorator使用方式
@log_text('excute')
def now_new():
    print('2020-06-02')

f = now_new
f()
#和两层嵌套的decorator相比，3层嵌套的效果是这样的：>>> now = log('execute')(now)

#练习，写一个装饰器，计算函数执行的时间
def metric(fn):
    def wrapper(*args, **kw):
        StartTime = time.time()
        r = fn(*args, **kw)
        EndTime = time.time()
        print('%s excuted in %s ms' %(fn.__name__, EndTime-StartTime))
        return r
    return wrapper

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        if gender not in ['male','female']:
            raise('TypeError', e)
        self.__gender = gender
