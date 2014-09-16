# coding=utf-8
'''
Created on 2014-9-16

@author: ruidge
'''
l = range(10)
print filter(lambda x: x >= 5 , l)
print filter(lambda x: x % 2 != 0 , l)
print '--------------'

name = ['milo', 'tom', 'jay']
age = (20, 21, 22)
tel = ['133', '186', 'abc']
other = ['o1', ['o21', 'o22', '023'], 'haha', 'hehe']
print zip(name, age, tel, other)  # 取最短的
print map(None, name, age, tel, other)  # None填充
print map(lambda *args:reduce(lambda x, y:str(x) + '-' + str(y) , args), name, age, tel, other) 
print '--------------'

r = range(101)
print reduce(lambda a, b:a + b, r)

