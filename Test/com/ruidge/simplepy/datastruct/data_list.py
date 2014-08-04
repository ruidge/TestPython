#coding=utf-8
'''
Created on 2014-7-21

@author: zhangrui6
'''
#列表中的项目应该包括在方括号中,是可变的数据类型
# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print 'I have', len(shoplist),'items to purchase.'
print 'I have', shoplist.__len__(),'items to purchase.'

print 'These items are:', # Notice the comma at end of the line
for item in shoplist:
    print item,

print '\nI also have to buy rice.'
shoplist.append('rice')
# shoplist = shoplist.__add__(["haha"]) #调用内置函数,同类型的add,不是item类型的添加
print 'My shopping list is now', shoplist

print 'I will sort my list now'
# 使用列表的sort方法来对列表排序。需要理解的是，这个方法影响列表本身，而不是返回一个修改后的列表——这与字符串工作的方法不同。
# 这就是我们所说的列表是 可变的 而字符串是 不可变的 
shoplist.sort(reverse = True)
print 'Sorted shopping list is', shoplist

print 'The first item I will buy is', shoplist[0]
olditem = shoplist[0]
del shoplist[0]
print 'I bought the', olditem
print 'My shopping list is now', shoplist
