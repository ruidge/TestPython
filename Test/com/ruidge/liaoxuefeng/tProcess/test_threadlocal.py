# coding=utf-8
'''
Created on 2015年2月9日

@author: zhangrui6
'''
import threading

class MyThreadLocal(threading.local):
    def __init__(self):
        self.num = 0

# 创建全局ThreadLocal对象:
local_school = MyThreadLocal()

def process_student():
    print 'Hello, name %s, num %s, (in %s)' % (local_school.studentName,local_school.num, threading.current_thread().name)

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.studentName = name
    local_school.num += 1 
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
# 这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。