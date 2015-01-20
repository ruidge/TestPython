# coding=utf-8
'''
Created on 2015-1-20

@author: zhangrui6
'''

import os
import glob

if __name__ == '__main__':
    cwd = os.getcwd()
    (a, b) = os.path.split(cwd)
    print a + '--' + b
    t_path = os.path.join(cwd, "aa.bb")
    print os.path.splitext(t_path)
    print "\n".join([k + "len:" + str(len(k)) for k in glob.glob1(cwd, "*.py")])
