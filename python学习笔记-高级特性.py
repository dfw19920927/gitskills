#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
L[:3]
#输出['Michael', 'Sarah', 'Tracy']
L[-2:]
#输出['Bob', 'Jack']
#倒数第一个元素的索引是-1
L=list(range(100))
L[::5]
'''输出[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 
50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
对tuple和字符串也适用
'''

#练习：利用切片，实现对字符串去除首尾空格
def trime(s):
	while s[:1]=='':
		s=s[1:]
	while s[-1:]=='':
		s=s[:-1]
	return s


#迭代：通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）
#默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，
#如果要同时迭代key和value，可以用for k, v in d.items()

#通过collections模块的Iterable类型判断对象是否为可迭代对象
from collections import Iterable
isinstance('abc',Iterable)
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
'''输出
1 1
2 4
3 9
'''
#练习：
def FindMinAndMax(L):
	if len(L)==0:
        return (None,None)
    else:
        max=L[0]
        min=L[0]
        for i in L:
            if i>max:
                max=i
            if i<min:
                min=i
        return(min,max)

#列表生成式
[x*x for x in range(1,20)]
[x*x for x in range(1,20) if x % 2 ==0]
[m+n for m in 'ABC' for n in 'XYZ']
d = {'x': 'A', 'y': 'B', 'z': 'C' }
[k+'='+v for k,v in d.items()]
[x if x % 2 == 0 else -x for x in range(1, 11)]
#输出[-1,2,-3,4,-5,6,-7,8,-9,10]
#练习：
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[x.lower() for x in L1 if isinstance(x,str)]

#生成器generator
'''L = [x * x for x in range(10)]
>>> L
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x1022ef630>

通过next()函数获得generator的下一个返回值
>>> next(g)
0
>>> next(g)
1
>>> next(g)
4
>>> next(g)
9
>>> next(g)
16
>>> next(g)
25
>>> next(g)
36
>>> next(g)
49
>>> next(g)
64
>>> next(g)
81
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
'''
'''
也可以用for循环打印
g=(x*x for x in range(10))
for n in g:
    print(n)
输出0,1,4,9...81
'''

#斐波那契数列1,1,2,3,5,8,13,21,34...
#基础写法
def fib(max):
	n,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,a+b
		n=n+1
	return 'done'
	
#生成器写法
def fib(max):
	n,a,b=0,0,1
	while(n<max):
		yield b
		a,b=b,a+b
		n=n+1
	return 'done'
'''这里，最难理解的就是generator和函数的执行流程不一样。
函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
再次执行时从上次返回的yield语句处继续执行
'''