#coding=utf-8
'''
Created on 2014-8-4

@author: zhangrui6
'''
import StringIO 
s = StringIO.StringIO("JGood is a handsome boy") 
s.write("JGood is a handsome boy \r\n") 
s.write('okkkk中国') 
s.seek(0) 
print s.read() 
print s.len
print s.pos
print "-----------------------"  
s.seek(-6, 2)  #U8为最后6个字节...
print s.read() 
 
#---- 结果 ---- 
#JGood is a handsome boy  
#okkkk中国 
#中国 
