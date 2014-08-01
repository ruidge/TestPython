# coding=utf-8
'''
Created on 2014-8-1

@author: zhangrui6
'''
class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: %s)' % self.name

    def tell(self):
        '''Tell my details.'''
        print 'Name:"%s" Age:"%s"' % (self.name, self.age),

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: %s)' % self.name

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: "%d"' % self.salary

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        #类似于super,但是得显式调用,通过类名调用,将self作为形参传过去.
        SchoolMember.__init__(self, name, age) 
        self.marks = marks
        print '(Initialized Student: %s)' % self.name

    def tell(self):
        SchoolMember.tell(self)
        print 'Marks: "%d"' % self.marks

t = Teacher('zhangsan', 40, 30000)
s = Student('lisi', 22, 75)

print  # prints a blank line

members = [t, s]
for member in members:
    member.tell()  # works for both Teachers and Students
# 相关知识点
# 为了使用继承，我们把基本类的名称作为一个元组跟在定义类时的类名称之后。然后，我们注意到基本类的__init__方法专门使用self变量调用，
# 这样我们就可以初始化对象的基本类部分。这一点十分重要——Python不会自动调用基本类的constructor，你得亲自专门调用它。
# 
# 我们还观察到我们在方法调用之前加上类名称前缀，然后把self变量及其他参数传递给它。
# 
# 注意，在我们使用SchoolMember类的tell方法的时候，我们把Teacher和Student的实例仅仅作为SchoolMember的实例。
# 
# 另外，在这个例子中，我们调用了子类型的tell方法，而不是SchoolMember类的tell方法。可以这样来理解，Python总是首先查找对应类型的方法，
# 在这个例子中就是如此。如果它不能在导出类中找到对应的方法，它才开始到基本类中逐个查找。基本类是在类定义的时候，在元组之中指明的。
# 
# 一个术语的注释——如果在继承元组中列了一个以上的类，那么它就被称作 多重继承 。

# 关于python中的抽象类和接口 
# From : http://bbs.chinaunix.net/thread-771123-1-1.html
# java中的抽象类是为了实现c++中的抽象类和模板之类的东西
# 接口是为了解决java不能多继承的问题
# 
# 很显然楼主是从java才开始接触面向对象程序设计的。实际上java的“接口”是一个特例而非普通现象。如果可以多继承的话，那还要接口干什么？
# 
# 实际上python才是最符合现实逻辑的“面向对象”
# python允许多继承，正如现实中，你既是公民也是纳税人，我们直接使用这些“类”而不需要特别的创建什么“纳税人接口”
# python中所有的类，都是抽象类，或者说根本不存在抽象类，类方法可以直接使用，“类”本身在定义的时候就已经实例化，你可以通过输入：某类[回车]看到其内存句柄。这是符合事实的，并且时简约明了的。
# 而在C++和java当中，一个类定义了以后，肯定是占用了内存空间，但是同时他又没有实例化，如果要使用的话还得实例化一次，又要占用一些内存空间。而类定义所占用的内存空间，使用率很低。
# python中不存在“基类”的概念，也没有单根，更没有基本类型，所有的一切都是对象。
# python是无神论的最完美体现，没有亚当，没有上帝，没有鬼神，没有唯一的主。你爱信什么信什么，爱是什么是什么，没有任何约束，但是不能存在特殊。
# 
# 另外，python根本没有意义去模仿java的接口，因为那完全没必要，python的标准类就完全包含java中的接口的所有功能。倒是模仿一下c++的模板会有些实际用途。

# 另:java中接口逻辑上是全是抽象函数的类,所以py中可以用空实现的方法做框架类
