#coding=utf-8
'''
Created on 2015年2月3日

@author: zhangrui6
'''

import struct

if __name__ == "__main__":
    f = open(r"C:\Users\zhangrui6\Desktop\classes.dex","rb")
    f.seek(88)
    s = f.read(4)
    
    print type(s)
    print s
    r = struct.unpack('<I', s)
    print r
    print struct.unpack('>I', s)
