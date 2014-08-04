#coding=utf-8
'''
Created on 2014-8-4

@author: zhangrui6
'''
import os

# os.name字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。
print os.name
# os.getcwd()函数得到当前工作目录，即当前Python脚本工作的目录路径。
print os.getcwd()
# os.getenv()和os.putenv()函数分别用来读取和设置环境变量。
# os.listdir()返回指定目录下的所有文件和目录名。
# os.remove()函数用来删除一个文件。
# 
# os.system()函数用来运行shell命令。
os.system("echo %path%")
# os.linesep字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'。
print os.linesep
# os.path.split()函数返回一个路径的目录名和文件名。
print os.path.split(r'e:/test/poem.txt')
# >>> os.path.split('/home/swaroop/byte/code/poem.txt')
# ('/home/swaroop/byte/code', 'poem.txt')
# 
# os.path.isfile()和os.path.isdir()函数分别检验给出的路径是一个文件还是目录。类似地，os.path.existe()函数用来检验给出的路径是否真地存在。