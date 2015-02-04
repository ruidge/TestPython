#coding=utf-8
'''
Created on 2015年2月2日

@author: zhangrui6
'''
import re

if __name__ == "__main__":
    r1 = re.split(r'\s+', 'a b   c')
    print r1
    r1 = re.split(r'[\s\,]+', 'a,b, c  d')
    print r1

    print "######"
    
    m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
    print m.groups()
    print m.group(0)
    print m.group(1)
    print m.group(2)

    print "######"

    #由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了
    print re.match(r'^(\d+)(0*)$', '102300').groups()
    #必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：
    print re.match(r'^(\d+?)(0*)$', '102300').groups()
    
    print "######"

    re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
    g1= re_telephone.match('010-12345').groups()
    print type(g1)
    print g1
    print g1[0]
    print g1[1]
    print re_telephone.match('010-8086').groups()
    
    