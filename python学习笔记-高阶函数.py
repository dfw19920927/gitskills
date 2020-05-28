from functools import reduce
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