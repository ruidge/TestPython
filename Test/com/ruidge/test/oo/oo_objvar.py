# coding=utf-8
'''
Created on 2014-8-1

@author: zhangrui6
'''
import time

class Person:
    #Person.population的时候为类的域 self.population的时候为对象的域
    population = 0 
    age = 0

    def __init__(self, name, age=100):
        self.name = name
        self.age = age
        print '(Initializing %s)' % self.name

        # When this person is created, he/she
        # adds to the population
        Person.population += 1

    def __del__(self):#__init__的相反
        print '%s says bye.' % self.name

        Person.population -= 1

        if Person.population == 0:
            print '%s is the last one.' % self.name
        else:
            print 'There are still %d people left.' % Person.population

    def sayHi(self):
        '''Greeting by the person.

        Really, that's all it does.'''
        print 'Hi, my name is %s.age is %s' % (self.name, self.age)

    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print 'I am the only person here.'
        else:
            print 'We have %d persons here.' % Person.population

zhangsan = Person('zhangsan')
zhangsan.sayHi()
zhangsan.howMany()

lisi = Person('lisi', 20)
lisi.sayHi()
lisi.howMany()

zhangsan.sayHi()
zhangsan.howMany()
del lisi
i = 5
while i > 0:
    print i
    i = i - 1
    time.sleep(1)
del zhangsan

