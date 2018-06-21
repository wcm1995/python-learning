#编写一个prod()函数，可以接受一个list并利用reduce()求积：
'''from functools import reduce
def prod(L):
    return reduce(lambda x,y:x*y,L)
print (prod([3,5,7,9]))'''


#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce
def str2float(s):
	def fn(x,y):
		return x*10+y
	n=s.index('.')
	s1=list(map(int,[x for x in s[:n]]))
	s2=list(map(int,[x for x in s[n+1:]]))
	return reduce(fn,s1)+reduce(fn,s2)/10**len(s2)
print('\'123.4567\'=',str2float('123.4567'))


