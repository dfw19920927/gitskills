#函数参数
#默认参数
def power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
#参数‘n’默认值为2，power(5)=power(5,2)=25
'''慎用默认参数'''
def add_end(L=[]):
	L.append('END')

add_end([1,2,3])
#输出[1,2,3,'END']
add_end()
#输出['END']
add_end()
#输出['END','END']
'''
python 函数在定义的时候，默认参数L的值就已经被计算出来了，即[],
因为默认参数L也是一个变量，它指向对象[]，每次调用了该函数，如果修改了L的内容
则下次调用时，默认参数的内容就变了，不再是一开始定义的[]了
'''
#修改
def add_end_1(L=None):
	if L is None:
		L=[]
	L.append('END')
	return L

#可变参数
def calc(*numbers):
	sum=0
	for n in numbers:
		sum+=n
	return sum

num1=[1,2,3]
num2=(1,2,3)
calc(*num1)
calc(*num2)
#均输出6

#关键字参数
def person(name,age,**kw):
	print('name:',name,'age:',age,'others:',kw)

person('Bob',35,city='Shenzhen')
#输出name: Bob age: 35,other: {'city': 'Beijing'}
extra={'city':'Shenzhen','job':'Engineer'}
person('jack',25,**extra)
#输出name: Jack age: 24,other: {'city': 'Beijing', 'job': 'Engineer'}
'''
如果要限制关键字参数的名称，需要使用命名关键字
命名关键字参数必须传入参数名称
'''
def person_1(name,age,*,city,job):
	print(name,age,city,job)
person('Bob',23,city='Shenzhen',job='Engineer')
#输出 Bob，23，Shenzhen，Engineer



#练习
def product(*nums):
	if len(nums)<=0:
		raise(TypeError,'参数为空')
	prod=1
	for n in nums:
		prod*=n
	return prod