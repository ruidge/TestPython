# coding=utf-8
'''
Created on 2014-8-1

@author: zhangrui6
'''
from abc import ABCMeta, abstractmethod

# 抽象类
class Headers(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.headers = ''

    @abstractmethod
    def _getBaiduHeaders(self):
        pass
    
    @abstractmethod
    def abstract_method_a(self):
        pass
    
    def __str__(self):
        return str(self.headers)

    def __repr__(self):
        return repr(self.headers)

# 实现类
class BaiduHeaders(Headers):
    def __init__(self, url, username, password):
        self.url = url
        self.headers = self._getBaiduHeaders(username, password)

    def _getBaiduHeaders(self, username, password):
        print 'implements abstract method'
#         client = GLOBAL_SUDS_CLIENT.Client(self.url)
#         headers = client.factory.create('ns0:AuthHeader')
#         headers.username = username
#         headers.password = password
#         headers.token = _baidu_headers['token']
#         return headers

if __name__ == '__main__':
    h = BaiduHeaders("", "", "")
    
# link : http://www.cnblogs.com/bjdxy/archive/2012/11/15/2772119.html
