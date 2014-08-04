#coding=utf-8
'''
Created on 2014-7-16

@author: ruidge
'''
#默认参数值应该是一个参数。更加准确的说，默认参数值应该是不可变的
def say(message, times = 1):
    print message * times

say('Hello')
say('World', 5)

# 只有在形参表末尾的那些参数可以有默认参数值，即你不能在声明函数形参的时候，先声明有默认值的形参而后声明没有默认值的形参。
# 这是因为赋给形参的值是根据位置而赋值的。例如，def func(a, b=5)是有效的，但是def func(a=5, b)是 无效 的。(掉func(xx)的时候把xx赋值给a):