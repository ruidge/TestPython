#coding=utf-8
'''
Created on 2015年2月5日

@author: zhangrui6
'''
def inc(x):
    def incx(y):
        return x+y
    return incx
 
inc2 = inc(2)
inc5 = inc(5)
 
print inc2(5) # 输出 7
print inc5(5) # 输出 10
print type(inc2)
print type(inc5)