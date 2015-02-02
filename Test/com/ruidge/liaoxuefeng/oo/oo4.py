#coding=utf-8
'''
Created on 2015年2月1日

@author: ruidge
'''
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

class Hello1(object):
    def fn(self, name='world'): # 先定义函数
        print('Hello, %s.' % name)
    

if __name__ == "__main__":
    Hello = type('Hello', (object,), dict(hello=fn)) # 动态创建Hello class 与写代码等效
    h = Hello()
    h.hello()
    print type(Hello)
    print type(h)
    h1 = Hello1()
    print type(Hello1)
    print type(h1)