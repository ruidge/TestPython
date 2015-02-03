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
    print "\n".join([k + "len:" + s(len(k)) for k in glob.glob1(cwd, "*.py")])
    print "------------------"
    f = open("C:\\Users\\zhangrui6\\Desktop\\test.mp3")
    print "tell() " , f.tell()
    print f.seek(-128, 2)
    print "tell() " , f.tell()
    print f.read(128)
    print "tell() " , f.tell()
    print f.read(128)
    print "tell() " , f.tell()
    print "is closed" , f.closed
    print f.close()
    print "is closed" , f.closed
    print f.close()
    try:
        print f.tell()
    except Exception, e:
        print e
