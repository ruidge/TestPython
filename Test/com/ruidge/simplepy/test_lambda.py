#coding=utf-8
'''
Created on 2014-9-14

@author: ruidge
'''
# f 接受lambda表达式为匿名函数,:前面为参数,:后面运算过程
f = lambda x, y:x * y
print f(2, 3)
print '-----------'

# 阶乘的两种方法
# def f(n):
#     if n > 0:
#         return n * f(n - 1)
#     else:
#         return 1
# print f(5)

i = range(1,6)
print i
print reduce(lambda x, y:x * y,i)