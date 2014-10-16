# coding=utf-8
'''
Created on 2014-10-16

@author: zhangrui6
'''
# 复合逻辑判断判断的'就近原则'
# 空的序列,字典,0表示false,其他情况表示true
print "a" and "b"
print "a" or "b"
# java中的 boolean ? a : b;
# 安全使用 and-or 技巧
a = ""
b = "second"
print (1 and [a] or [b])[0] #lambda 中不允许使用if条件判断,可以使用and-or简单代替

# split 不带参数
s = "this   is\na\ttest" #空格 换行符 制表符号
print s
print s.split()           #对空白进行分割
print " ".join(s.split()) 
