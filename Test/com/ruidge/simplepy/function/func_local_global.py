#coding=utf-8
'''
Created on 2014-7-16

@author: ruidge
'''
def func(x):
    print 'x is', x
    x = 2
    print 'Changed local x to', x
 
x = 50
func(x)
print 'x is still', x
print '-----------------'
# def func():
#     #外部没有定义会报错,不推荐使用全局定义
#     global x
# 
#     print 'x is', x
#     x = 2
#     print 'Changed local x to', x
# 
# x = 50
# func()
# print 'Value of x is', x