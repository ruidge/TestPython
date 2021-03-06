# coding=utf-8
'''
Created on 2014-8-4

@author: zhangrui6
'''

class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    d = raw_input('Enter something --> ')
    if len(d) < 3:
        raise ShortInputException(len(d), 3)
    # Other work can continue as usual here
except EOFError:
    print '\nWhy did you do an EOF on me?'
except ShortInputException, x:
    print 'ShortInputException: The input was of length %d, \
    was expecting at least %d' % (x.length, x.atleast)
else:
    print 'No exception was raised.'
finally:
    print 'finally statement executing'