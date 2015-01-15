# coding=utf-8
'''
Created on 2015-1-15

@author: zhangrui6
'''
class counter:
    count = 0                     
    def __init__(self):
        self.__class__.count += 1
    def __sayPrivate(self):
        print 'hello private'
    def sayPublic(self):
        print 'hello public'
# 如果一个 Python 函数，类方法，或属性的名字以两个下划线开始 (但不是结束)，它是私有的；其它所有的都是公有的。 
# Python 没有类方法保护 的概念 (只能用于它们自已的类和子类中)。类方法或者是私有 (只能在它们自已的类中使用) 或者是公有 (任何地方都可使用)。
# 
# 在 MP3FileInfo 中，有两个方法：__parse 和 __setitem__。正如我们已经讨论过的，__setitem__ 是一个专有方法；
# 通常，你不直接调用它，而是通过在一个类上使用字典语法来调用，但它是公有的，并且如果有一个真正好的理由，你可以直接调用它 (甚至从 fileinfo 模块的外面)。
# 然而，__parse 是私有的，因为在它的名字前面有两个下划线。
if __name__ == '__main__':
    print counter.count
    c = counter()
    print counter.count
#     print c.sayPublic()
    print c.__sayPrivate()
