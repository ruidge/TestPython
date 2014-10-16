#coding=utf-8
'''
Created on 2014-10-16

@author: zhangrui6
'''
import string
import test_apihelper
import __builtin__

if __name__ == "__main__":
    li = ['a','b','c']
    print li.pop()
    print 'after 1:' , li
    print getattr(li, "pop") #没有执行pop
    print getattr(li, "pop")() #执行了pop
    getattr(li, "append")("Moe")#执行了append添加到的末尾
    print 'after 2:' , li
    print getattr({}, "clear") 
    print getattr({}, "haha","clear") #第二个函数不存在的时候,第三个作为缺省值,否则会抛异常
    #通常，getattr(object, "attribute") 等价于 object.attribute。
    #如果 object 是一个模块的话，那么 attribute 可能是定义在模块中的任何东西：函数、类或者全局变量


# getattr 作为一个分发者
# getattr 常见的使用模式是作为一个分发者。举个例子，如果你有一个程序可以以不同的格式输出数据，
# 你可以为每种输出格式定义各自的格式输出函数，然后使用唯一的分发函数调用所需的格式输出函数。
# 例如，让我们假设有一个以 HTML、XML 和普通文本格式打印站点统计的程序。
# 输出格式在命令行中指定，或者保存在配置文件中。statsout 模块定义了三个函数：
# output_html、output_xml 和 output_text。然后主程序定义了唯一的输出函数，如下：
# 
# import statsout
# 
# def output(data, format="text"):                              
#     output_function = getattr(statsout, "output_%s" % format, statsout.output_text)
#     return output_function(data)
#
# getattr 自省的核心, 有点类似于java中的反射