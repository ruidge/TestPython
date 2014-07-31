#coding=utf-8
'''
Created on 2014-7-21

@author: zhangrui6
'''
#序列包括字符串'',列表[],元组(),字典{}
# 序列的两个主要特点是索引操作符和切片操作符。
# 索引操作符让我们可以从序列中抓取一个特定项目。切片操作符让我们能够获取序列的一个切片，即一部分序列。
shoplist = ['apple', 'mango', 'carrot', 'banana','apple']

# Indexing or 'Subscription' operation 
#dict []中只能是key值,不存在的key值报KeyError: 列表和原则int越界报IndexError
print 'Item %s is %s' % (shoplist.index('apple', 1 ),shoplist[0])
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1]
print 'Item -2 is', shoplist[-2]
# print 'Item 100 is', shoplist[100]
print '------------'

# Slicing on a list
print 'Item 1 to 3 is', shoplist[1:3]
print 'Item 2 to end is', shoplist[2:]
print 'Item 1 to -1 is', shoplist[1:-1]
print 'Item start to end is', shoplist[:]
print '------------'

# Slicing on a string
name = 'swaroop'
print 'characters 1 to 3 is', name[1:3]
print 'characters 2 to end is', name[2:]
print 'characters 1 to -1 is', name[1:-1]
print 'characters start to end is', name[:]
print 'characters start to end step 2 is', name[::2]
print '------------'


#对象引用,想要复制序列需要用切片进行复制操作
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist # mylist is just another name pointing to the same object!

del shoplist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist
# notice that both shoplist and mylist both print the same list without
# the 'apple' confirming that they point to the same object

print 'Copy by making a full slice'
mylist = shoplist[:] # make a copy by doing a full slice
del mylist[0] # remove first item

print 'shoplist is', shoplist
print 'mylist is', mylist
# notice that now the two lists are different

print 'join function',"--".join(shoplist)
