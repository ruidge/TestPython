# coding=utf-8
'''
Created on 2014-9-16

@author: ruidge
'''
l = range(10)
#map:函数作用于序列的每一项值,把返回结果是False的过滤掉
print filter(lambda x: x >= 5 , l)
print filter(lambda x: x % 2 != 0 , l)
print '--------------'

name = ['milo', 'tom', 'jay']
age = (20, 21, 22)
tel = ['133', '186', 'abc']
other = ['o1', ['o21', 'o22', '023'], 'haha', 'hehe']
print zip(name, age, tel, other)  # 取最短的
#map:函数作用于序列的每一项值
print map(None, name, age, tel, other)  # None填充
print map(lambda *args:reduce(lambda x, y:str(x) + '-' + str(ys args), namesge, tel, other) 
print '--------------'

r = range(101)
#reduce:函数作用于序列的每两项值,并将结果与下一个作用,知道整个列表结束
print reduce(lambda a, b:a + b, r)
def func(x):
    if x <= 1 :
        return False
    found = False
    for i in range(2,x -1 ):
        if(x % i == 0):
            found = True
            break
        else:
            continue
    return not found
print filter(func,r)

