# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。

def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


from functools import reduce
def prod(L):
    return reduce(lambda x,y:x*y,L)
print (prod([3,5,7,9]))
