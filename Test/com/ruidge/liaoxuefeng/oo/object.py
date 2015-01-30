# coding=utf-8
'''
Created on 2015年1月30日

@author: zhangrui6
'''
# py 2.2 后继承 object 的目的是使这个类成为 new style class, 没有继承 object 的为传统 classic class,
class Foo(object):
    pass

class Foo1:
    pass

if __name__ == "__main__":
    print type(Foo), type(Foo1)
    print isinstance(Foo, object)
    print isinstance(Foo1, object)
    print dir(Foo)
    print dir(Foo1)
    
