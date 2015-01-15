#coding=utf-8
'''
Created on 2015-1-15
    
@author: zhangrui6
'''
class ClassA:
    '''三引号的注释'''
    pass
    
    fieldA = []
    "二引号注释"

    def funcA(self):
        '单引号注释'
        pass
    
if __name__ == '__main__':
    classA = ClassA()
    print classA.__doc__
    print
    print classA.fieldA.__doc__
    print
    print classA.funcA.__doc__