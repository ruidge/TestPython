# coding=utf-8
'''
Created on 2015年2月4日

@author: zhangrui6
'''

def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
@log
def now():
    print '2013-12-25'
    
if __name__ == "__main__":
    pass