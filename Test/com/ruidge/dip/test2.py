#coding=utf-8
'''
Created on 2014-10-17

@author: zhangrui6
'''
import os
from os import name #尽量少用

def haha():
    "this is empty function"
    pass

if __name__ == "__main__":
    print os.curdir
    print name
    print haha.__doc__