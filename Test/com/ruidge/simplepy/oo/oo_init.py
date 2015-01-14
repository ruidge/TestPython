# coding=utf-8
'''
Created on 2014-7-21

@author: zhangrui6
'''
# 创建一个int对象,不像java存在基本类型,一切都是对象
# help(int)
# a = int(15)
# b = 22
# print hex(16)
# print a.__hex__()
# print b.__hex__()
# print a.__add__(10)

# __init__方法类似于C++、C#和Java中的 constructor 。
class Person:
    name = 'ruidge'
#     def __init__(self):
#         print r'__init__(self)'
    def __init__(self, age=10):  # 构造函数,不需要声明域,直接进行赋值...只能有一个构造函数
        self.age = age
        print r'__init__(self,age = ' + str(self.age) + ')'
    
    def sayHi(self):  # self表示自己,类似java中的this
        print 'name is %s , age is %d' % (self.name, self.age)
        
p = Person()  # 没有缺省的构造函数
p = Person(100)  # 直接调用'构造函数'创建对象
p.name = 'zhangsan'
# p.age = 90
p.sayHi()
print p 
print type(p)  # <type 'instance'>
print type(Person)  # <type 'classobj'>
