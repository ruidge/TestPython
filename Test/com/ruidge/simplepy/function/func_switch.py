# coding=utf-8
'''
Created on 2014-9-15

@author: ruidge
'''
from __future__ import division

# python没有内置的switch语句,可以用字典实现同样的功能
def plus(x, y):
    return x + y
def minus(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

# 充分体现了一切皆对象的理念,函数也可以使对象
f = {'+':plus, '-':minus, '*':multiply, '/':divide }
print f['+'](3, 2)
print f['-'](3, 2)
print f['*'](3, 2)
print f['/'](3, 2)
