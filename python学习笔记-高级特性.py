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


