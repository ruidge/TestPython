#coding=utf-8
'''
Created on 2015年2月5日

@author: zhangrui6
'''
age = 25
name = 'Caroline'
 
print('{0} is {1} years old. '.format(name, age)) #输出参数
print('{0} length is {1}. '.format(name, len(name))) 
print('{0} is a girl. '.format(name))
print('{0:.3} is a decimal. '.format(1.0/3)) #小数点后三位
print('{0:_^11} is a 11 length. '.format(name)) #使用_补齐空位
print('{first} is as {second}. '.format(first=name, second='Wendy')) #别名替换
print('My name is {0.name}'.format(open('out.txt', 'w'))) #调用方法
print('My name is {0:8}.'.format('Fred')) #指定宽度