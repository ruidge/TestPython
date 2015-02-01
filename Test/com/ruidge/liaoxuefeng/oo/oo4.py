#coding=utf-8
'''
Created on 2015年2月1日

@author: ruidge
'''
def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

if __name__ == "__main__":
    Hello = type('Hello', (object,), dict(hello=fn)) # 动态创建Hello class
    h = Hello()
    h.hello()
    print type(Hello)
    print type(h)