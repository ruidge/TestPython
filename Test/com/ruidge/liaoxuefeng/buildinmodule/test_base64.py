#coding=utf-8
'''
Created on 2015年2月3日

@author: zhangrui6
'''
import base64
print base64.b64encode('binary\x00string')
print base64.b64encode('binary\x00\x00string')
print base64.b64encode('binary\x00\x00\x00string')
print base64.b64decode('YmluYXJ5AHN0cmluZw==')
print base64.b64decode('YmluYXJ5AABzdHJpbmc=')
print base64.b64decode('YmluYXJ5AAAAc3RyaW5n')
