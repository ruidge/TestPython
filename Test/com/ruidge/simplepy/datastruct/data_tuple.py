#coding=utf-8
'''
Created on 2014-7-21

@author: zhangrui6
'''
zoo = ('wolf', 'elephant', 'penguin')
print 'Number of animals in the zoo is', len(zoo)
# print 'Number of animals in the zoo is', zoo.__len__();

new_zoo = ('monkey', 'dolphin', zoo)
print 'Number of animals in the new zoo is', len(new_zoo)
print 'All animals in new zoo are', new_zoo
print 'Animals brought from old zoo are', new_zoo[2]
print 'Last animal brought from old zoo is', new_zoo[2][2]
print 'Last animal brought from old zoo is', new_zoo[-1][-1]
# print 'new zoo index', new_zoo[-4]#错误...IndexError越界


print '-------------------------------'
# 一个空的元组由一对空的圆括号组成，如myempty = ()。
# 然而，含有单个元素的元组就不那么简单了。你必须在第一个（唯一一个）项目后跟一个逗号，
# 这样Python才能区分元组和表达式中一个带圆括号的对象。即如果你想要的是一个包含项目2的元组的时候，你应该指明singleton = (2 , )。
singleton = (2 , )
# singleton = (2) #报TypeError: 'int' object has no attribute '__getitem__'
# print type(singleton)
print singleton[0]

print '--------------打印时候格式化用法-----------------'
age = 26
name = 'ruidge'

print '%s is %s years old' % (name, age)
print 'Why is %s playing with that python?' % name # ==(name, )
