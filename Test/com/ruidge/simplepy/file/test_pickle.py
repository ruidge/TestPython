# coding=utf-8
'''
Created on 2014-8-4

@author: zhangrui6
'''
import cPickle as p
# import pickle as p

# Python提供一个标准的模块，称为pickle。使用它你可以在一个文件中储存任何Python对象，之后你又可以把它完整无缺地取出来。这被称为 持久地 储存对象。
# 还有另一个模块称为cPickle，它的功能和pickle模块完全相同，只不过它是用C语言编写的，因此要快得多（比pickle快1000倍）。
# 我们把这两个模块都简称为pickle模块。

# shoplistfile = 'shoplist.data'
# the name of the file where we will store the object

shoplist = ['apple', 'mango', 'carrot','新的']
file_path = r'e:/test/shoplist.data'

# Write to the file
f = file(file_path, 'w') #a会写进去多个,但是只读出第一个
p.dump(shoplist, f)  # dump the object to a file
f.close()

del shoplist  # remove the shoplist

# Read back from the storage
f = file(file_path)
storedlist = p.load(f)
print storedlist
#---------------------------------------------------#
str = r'this is a string 这是一条字符串 \n'
file_path_str = r'e:/test/string.data'

# Write to the file
f = file(file_path_str, 'w') #a会写进去多个,但是只读出第一个
p.dump(str, f) 
f.close()

del str  # remove the str

# Read back from the storage
f = file(file_path_str)
storedstr = p.load(f)
print storedstr
