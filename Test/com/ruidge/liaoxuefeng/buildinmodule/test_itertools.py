#coding=utf-8
'''
Created on 2015年2月3日

@author: zhangrui6
'''
import time
import itertools

natuals = itertools.count(2,2)
natuals = itertools.repeat("123")
natuals = itertools.cycle({"ka":"va","kb":"vb"})
print type(natuals)
# for n in natuals:
#     time.sleep(1)
#     print n
# for n in natuals:
#     time.sleep(1)
#     print n
for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, list(group) 
print "####"
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print key, list(group)
print "####"
for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: len(c)):
    print key, list(group)
print "####"
r = map(lambda x: x*x, itertools.count(1)) #oom
r = itertools.imap(lambda x: x*x, itertools.count(1)) #oom
for x in r:
    print x 