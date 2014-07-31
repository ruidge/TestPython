#coding=utf-8
'''
Created on 2014-7-18

@author: zhangrui6
'''
import module_sayhi
# 走else
# import module_name

if __name__ == '__main__':
    print 'This program is being run by itself'
    module_sayhi.sayHi()
    print module_sayhi.hello
else:
    print '__name__ is ' + __name__
    print 'I am being imported from another module'

# 每个Python模块都有它的__name__，如果它是'__main__'，这说明这个模块被用户单独运行，我们可以进行相应的恰当操作。

#不像Java没有入口的概念,导入的时候直接把里面的函数全执行了,
# 可以通过__name__=='__main__'判断是否是当前的模块 见test1