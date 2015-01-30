# coding=utf-8
'''
Created on 2015年1月30日

@author: zhangrui6
'''

# Python内置的@property装饰器就是负责把一个方法变成属性调用的

# 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，
class Student(object):
    @property
    def ppscore(self):
        return self._score

    @ppscore.setter
    def haha(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

if __name__ == "__main__":
    s = Student()
    #score的内部属性名字叫_score
    s.haha = 12 #实际调用@score.setter
    print s.ppscore #实际调用@property
