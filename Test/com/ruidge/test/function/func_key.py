#coding=utf-8
'''
Created on 2014-7-16

@author: ruidge
'''
def func(a, b=5, c=10):
    print 'a is', a, 'and b is', b, 'and c is', c
if __name__ == '__main__':
    func(1)
    func(3, 7)
    func(25, c=24)

    func(c=50, a=100)
    # func() #error

# 1.由于我们不必担心参数的顺序，使用函数变得更加简单了。
# 2.假设其他参数都有默认值，我们可以只给我们想要的那些参数赋值。
# 3.传形参时候不标明参数从前往后传,标明可以乱序传.