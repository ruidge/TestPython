#coding=utf-8
'''
Created on 2014-7-21

@author: zhangrui6
'''
#创建一个int对象,不像java存在基本类型,一切都是对象
help(int)
a = int(15)
b = 22
print hex(16)
print a.__hex__()
print b.__hex__()
print a.__add__(10)