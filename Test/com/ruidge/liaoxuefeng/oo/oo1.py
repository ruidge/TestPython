# coding=utf-8
'''
Created on 2015年1月30日

@author: zhangrui6
'''
import types

class Demo(object):
    pass
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性
class Ddemo(object):
    __slots__ = ("age",)

def set_name(self, name):  # 定义一个函数作为实例方法
    self.name = name

if __name__ == "__main__":
    d = Demo()
    # 动态添加属性
    d.name = "ruidge"
    print d.name  # 可以动态添加,没有属性抛AttributeError
    d.set_name = types.MethodType(set_name, d, Demo)  # 给实例绑定一个方法
    d.set_name("haha")  # 调用实例方法
    print d.name  # AttributeError
    
    types.MethodType(set_name, None, Demo)  # 给类绑定一个方法
    d1 = Demo()
    d1.set_name("d1")
    print d1.name

#     dd = Ddemo()
#     # 动态添加属性
#     dd.age = 12
#     print dd.age  
#     dd.name = "ruidge"
#     print dd.name  # 不在__slots__, 不可以动态添加
    
