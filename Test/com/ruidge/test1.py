#coding=utf-8
'''
Created on 2014-6-11

@author: ruidge
'''

import com.ruidge.test.function.func_key as haha
import com.ruidge.test.mokuai.module_name as hehe
import com.ruidge.test.mokuai.module_sayhi as aa

#不像Java没有入口的概念,导入的时候直接把里面的函数全执行了,
# 可以通过__name__=='__main__'判断是否是当前的模块

haha.func(1)

# module_name:
# if __name__ == '__main__':
#     print 'This program is being run by itself'
# else:
#     print 'I am being imported from another module'
aa.sayHi()
