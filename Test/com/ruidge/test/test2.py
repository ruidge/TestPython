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

ts = time.localtime()
for a in ts:
    print a,

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

if not os.path.exists('E:\\'):
    os.makedirs('E:\\test')
z = zipfile.ZipFile('E:\\test', mode="r", compression=zipfile.ZIP_STORED,
     allowZip64=False)