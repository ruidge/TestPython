# coding=utf-8
'''
Created on 2015年1月30日

@author: zhangrui6
'''

# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class Fib(object):
    def __init__(self, total):
        self.index = 0
        self.total = total
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.index >= self.total:  # 退出循环的条件
            raise StopIteration();
        self.index += 1
        return self.a  # 返回下一个值
    # 像序列下标和切片操作
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
# 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。
# 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
class Student(object):
    def __init__(self, name):
        self.name = name
        
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        elif attr == 'ageNum':
            return 16
#     __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，
# 把函数看成对象，因为这两者之间本来就没啥根本的区别。
# 如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的，这么一来，我们就模糊了对象和函数的界限。
    def __call__(self, n=1):
        
        print('My name is %s.' % self.name * n)
        
if __name__ == "__main__":
    f = Fib(10)
    for s in f:
        print s 
    print "###"
    print f[4], f[9]
    print "###"
    print f[4:9]
    print "###"
    s = Student("ruidge")
    print s.age()
    print s.ageNum
    print s(3)
    print "callable(s)" , callable(s) #callable判断是否是函数,类如果有__call__也算函数
    
