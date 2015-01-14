#coding=utf-8
'''
Created on 2014-10-16

@author: zhangrui6
'''
import string
import test_apihelper
import __builtin__

if __name__ == "__main__":
#     params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
#     s = ";".join(["%s=%s" % (k,v) for k,v in params.items()])
#     print s
#     
#     a = range(10)
#     b = [i*10 for i in a if i % 2 == 0]
#     print a
#     print b
#     
#     print type(type)
#     for i in dir():
#         print i

    #callable 是否可以被调用
    print (string.join)
    print (string.punctuation)
    print callable(string.join)
    print callable(string.punctuation)
     
    #显示所有__buildin__的内置函数
#     test_apihelper.info(__builtin__)
    
    