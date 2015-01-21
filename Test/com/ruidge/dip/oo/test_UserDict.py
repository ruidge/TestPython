# coding=utf-8
'''
Created on 2014-10-17

@author: zhangrui6
'''
from UserDict import UserDict
from UserList import UserList

class TestDict(UserDict):
    def __init__(self, aa, bb):
        UserDict.__init__(self)
        self["aa"] = aa
        self["bb"] = bb
#         习惯上，所有的数据属性都在 __init__ 方法中初始化为有意义的值。(建议)
#         然而，这并不是必须的，因为数据属性，像局部变量一样，当你首次赋给它值的时候突然产生。
        
#直接继承自内建数据类型 dict,不必导包,也不必显示调用父类的构造函数
class TestDict1(dict):
    def __init__(self, aa, bb):
        self["aa"] = aa
        self["bb"] = bb
        
class TestList(UserList):
    def __init__(self, aa, bb):
        UserList.__init__(self)
        self.append(aa)
        self.append(bb)
#          Python没有任何形式的函数重载。一个 __init__ 方法就是一个 __init__ 方法，不管它有什么样的参数。
#          每个类只能有一个 __init__ 方法，并且如果一个子类拥有一个 __init__ 方法，它总是 覆盖父类的 __init__ 方法，
#         甚至子类可以用不同的参数列表来定义它。

#         Python 的原作者 Guido 是这样解释方法覆盖的：“子类可以覆盖父类中的方法。因为方法没有特殊的优先级设置，
#             父类中的一个方法在调用同类中的另一方法时，可能其实调用到的却是一个子类中覆盖父类同名方法的方法。 
#             (C++ 程序员可能会这样想：所有的 Python 方法都是虚函数。)”
        
        
if __name__ == "__main__":
    td1 = TestDict("haha", 100)
    print td1
    print td1.get("aa", "aa")
    print td1.get("bb", "bb")
    print td1.get("cc", "cc")
    print td1
    print td1['aa']
    print "-----------------------------"
    print td1.__class__ is UserDict
    print td1.__class__ is TestDict #实例
    print isinstance(td1, UserDict) #实例或者子类
    
#     td2 = TestDict1("haha", 100)
#     print td2
#     print td2.get("aa", "aa")
#     print td2.get("bb", "bb")
#     print td2.get("cc", "cc")
#     print td2
#     print "-----------------------------"
#     tl1 = TestList("haha", 100)
#     print tl1.__len__()
#     print tl1
#     print tl1.pop()
#     print tl1
#     
#     aa = ['a','b','c']
#     import copy
#     bb = copy.copy(aa)
#     print aa
#     print id(aa)
#     print bb
#     print id(bb)
    



