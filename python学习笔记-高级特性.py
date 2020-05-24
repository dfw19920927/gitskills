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