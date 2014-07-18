#coding=utf-8
'''
Created on 2014-7-16

@author: ruidge
'''

# 文档字符串的惯例是一个多行字符串，它的首行以大写字母开始，句号结尾。第二行是空行，从第三行开始是详细的描述。
def max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    x = int(x) # convert to integers, if possible
    y = int(y)

    if x > y:
#         return x , 'is maximum' #可以但是会自动在外面加上一层括号(5, 'is maximum')
#         return x + ' is maximum' #不可以,不支持int和str的直接加法
        return str(x) + ' is maximum'#可以,先将int转为str类型
    else:
        return str(y) + ' is maximum'

print max(5, 3)
print max(5, '7')
print max.__doc__ #把函数当做对象去调用内部属性了...

# help(max) #其实DocStrings是help()打印出来的内容