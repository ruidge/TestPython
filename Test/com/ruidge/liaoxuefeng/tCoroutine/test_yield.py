# coding=utf-8
'''
Created on 2015年2月8日

@author: ruidge
'''
import time

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'

def produce(c):
    c.next()
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        rr = c.send(n)
        print('[PRODUCER] Consumer return: %s' % rr)
    c.close()

if __name__ == '__main__':
    c = consumer()
    produce(c)
