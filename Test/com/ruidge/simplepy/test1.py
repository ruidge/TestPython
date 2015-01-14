#coding=utf-8
'''
Created on 2014-6-11

@author: ruidge
'''

import com.ruidge.simplepy.function.func_key as haha
import com.ruidge.simplepy.mokuai.module_name as hehe
import com.ruidge.simplepy.mokuai.module_sayhi as aa

#不像Java没有入口的概念,导入的时候直接把里面的函数全执行了,
# 可以通过__name__=='__main__'判断是否是当前的模块

haha.func(1)

aa.sayHi()

print "aa", "bb" #加逗号自动空格连接字符串
aaa = {'11':'111','22':'222'}
print len(aaa)
# for k,v in aaa.items():
#     print k , "--", v
for a in aaa.items():
    print type(a)
    print a