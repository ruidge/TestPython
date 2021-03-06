#coding=utf-8
'''
Created on 2014-8-5

@author: zhangrui6
'''
def info(object, spacing=20, collapse=1):
    """Print methods and doc strings.
    
    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
#     methodList = [method for method in dir(object) if callable(method)] #无效
    processFunc = collapse and (lambda sd " ".join(sdsplit())) or (lambda sd sd#此处第一个lambda不可能为"",所以相当于一个collapse的if语句
    print "\n".join(["%s %s" %
d  d                  (method.ljust(spacing),
                       processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])

if __name__ == "__main__":
#     print info([],collapse = 0)
    print info('string',collapse = 1)
#     print dir(1) # 返回任意对象的属性和方法列表，包括模块对象、函数对象、字符串对象、列表对象、字典对象