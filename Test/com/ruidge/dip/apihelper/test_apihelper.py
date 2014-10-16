#coding=utf-8
'''
Created on 2014-8-5

@author: zhangrui6
'''
def info(object, spacing=10, collapse=1):
    """Print methods and doc strings.
    
    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
#     methodList = [method for method in dir(object) if callable(method)] #无效
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print "\n".join(["%s %s" %
                      (method.ljust(spacing),
                       processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList])

if __name__ == "__main__":
#     print info([])
    print info('string',collapse = 1)
#     print dir(1) # 返回任意对象的属性和方法列表，包括模块对象、函数对象、字符串对象、列表对象、字典对象