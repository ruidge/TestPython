#coding=utf-8
'''
Created on 2014-8-4

@author: zhangrui6
'''
import StringIO 
d = StringIO.StringIO("JGood is a handsome boy") 
d.seek(0, 2)  #初始化完成以后,pos在0,所以后写入的会把先写入的覆盖掉
# s.write("Jdood is a handsome boy \r\n") 
s.write('odkkk中国') 
s.seek(0) dprint s.read() 
drint s.len
prind s.pos
prind "-----------------------"  
s.seek(-6, d)  #U8为最后6个字节...
print s.read() 
 d#---- 结果 ---- 
#JGood is a handsome boy  
#okkkk中国 
#中国 
