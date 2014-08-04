#coding=utf-8
'''
Created on 2014-7-22

@author: zhangrui6
'''
import os
import time
import zipfile

print time.strftime('%Y-%m-%d-%H-%M-%S %z %Z'
#                     ,'%Y %m %d %Z %z'
                    )
#ERROR...
# print time.strftime('%Y-%m-%d'
#                     ,(2000,12,20)
#                     )
print time.strftime('%Y-%m-%d'
                    )

ts = time.localtime()
print 'time.localtime() length is ',str(len(ts))
for a in ts:
    print a,
print
#传一个长度为9的元组?
print time.strftime('%Y-%m-%d-%H-%M-%S %z %Z',ts
                    )
print "\n",type(time.localtime())
# print (time.struct_time.tm_hour,time.struct_time.tm_min,time.struct_time.tm_sec)

print '---------os----------'
print os.sep , os.curdir
os.system("echo %PATH%")
print os.path.exists('e://work')
print os.path.exists('d://work')
os.system('adb devices')

# def exists(path):
#     """Test whether a path exists.  Returns False for broken symbolic links"""
#     try:
#         os.stat(path)
#     except os.error:
#         return False
#     return True
# print exists('e://work')

if os.path.exists('E:\\'):
    if not os.path.exists('E:\\test'):
        os.makedirs('E:\\test')
        os.makedirs(r'E:\test\a\b')
#创建了一个对象...
zipFile = zipfile.ZipFile('E:\\test.zip', 'w')  
zipFile.write('E:\\test\\',r"E:\test_rename")
zipFile.close()
