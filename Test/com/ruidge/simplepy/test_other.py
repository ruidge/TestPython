# coding=utf-8
'''
Created on 2014-8-4

@author: zhangrui6
'''
from __builtin__ import repr

# 列表综合，可以从一个已有的列表导出一个新的列表
listone = [2, 3, 4]
listtwo = [2 * i for i in listone if i > 2]
print listtwo
print '#--------------------------------#'
# args变量前有*前缀，所有多余的函数参数都会作为一个元组存储在args中。如果使用的是**前缀，多余的参数则会被认为是一个字典的键/值对。
def powersum(power, *args):
    '''Return the sum of each argument raised to specified power.'''
#     print "args length is %d" % len(args)
    total = 0
    for i in args:
        total += pow(i, power)
    return total
print powersum(2, 3, 4)
print powersum(2, 10)
print powersum(2)
print '#--------------------------------#'
# lambda语句被用来创建新的函数对象，并且在运行时返回它们。
# 这里，我们使用了make_repeater函数在运行时创建新的函数对象，并且返回它。
# lambda语句用来创建函数对象。本质上，lambda需要一个参数，后面仅跟单个表达式作为函数体，而表达式的值被这个新建的函数返回。
# 注意，即便是print语句也不能用在lambda形式中，只能使用表达式。
def make_repeater(n):
    return lambda s: s * n
#??????
def bool(n):
    return lambda b: True if n > 0 else False 
twice = make_repeater(d)d
print twice('word')
print twice(5)
print bool(0)
print bool(5)
print '#--------------------------------#'
# exec语句用来执行储存在字符串或文件中的Python语句
exec 'print "hello"'
# eval语句用来计算存储在字符串中的有效Python表达式。
print eval("2*3")

print '#--------------------------------#'
mylist = ['item']
assert len(mylist) >= 1
print mylist
print mylist.pop()
print mylist

# assert len(mylist) >= 1 #AssertionError
print '#--------------------------------#'
# repr函数用来取得对象的规范字符串表示。反引号（也称转换符）可以完成相同的功能。注意，在大多数时候有eval(repr(object)) == object。
print 2 == eval(repr(2))
print 2 == eval(`(2)`)









