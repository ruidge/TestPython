# coding=utf-8
'''
Created on 2014-8-4

@author: zhangrui6
'''

poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
        use Python!
'''
file_path = r'e:/test/poem.txt'
# f = file('poem.txt', 'w')  # 将文件创建在当前py文件所在的目录下
f = file(file_path, 'a')  
f.write(poem)  # write text to file
f.close()  # close the file

f = file(file_path)
# if no mode is specified, 'r'ead mode is assumed by default
while True:
    line = f.readline()
    if len(line) == 0:  # Zero length indicates EOF
        break
    print line,
    # Notice comma to avoid automatic newline added by Python
f.close()  # close the file
