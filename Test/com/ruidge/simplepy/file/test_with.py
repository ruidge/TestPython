# coding=utf-8
'''
Created on 2015年2月10日

@author: zhangrui6
'''
import time

class Sample:
    def __enter__(self):
        print "In __enter__()"
        return "Foo"
 
    def __exit__(self, exctype, excvalue, traceback):
        print "exctype",exctype
        print "excvalue",excvalue
        print "traceback",traceback
        print "In __exit__()"
 
 
def get_sample():
#     写这里直接挂掉
#     e = 1 / 0
    return Sample()
 
if __name__ == "__main__":
    with get_sample() as sample:
        time.sleep(1)
#        写这里异常后__exit__还会走到并传过去,但是print没有走到
        e = 1 / 0
        print "sample:", sample

# 紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。
# 当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。