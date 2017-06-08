#!/usr/bin/python# -*- coding:UTF-8 -*-

# 这个文件学习简明Python教程的11章 - 面向对象编程
"""
注意：
1. int也是类
2. iOS(属性) -> Python(域)  方法 -> 方法
Python(域 + 方法) -> Python(属性)
域分：实例变量 和 类变量
"""

# 定义对象方法
class Person:
    population = 0 # 类域
    def sayHello(self):
        print 'Are you OK?', self.name

    def howMany(self):
        if Person.population == 1:
            print 'I am the only person here'
        else:
            print 'We have %d person here' % Person.population

    # 生命周期方法 - init方法
    def __init__(self, name):
        self.name = name # 对象域
        Person.population += 1

    # 生命周期方法 - 对象释放的时候调用 deloc
    # 这个方法会在对象不再被使用的时候自动调用，也可以手动调用
    def __del__(self):
        '''I am dying.'''
        print '%2 says bye.' % self.name
        Person.population -= 1

        if Person.population == 0:
            print 'I am the last one.'
        else:
            print 'There are still %d people left.' % Person.population

p = Person("哈哈哈")
p.sayHello()
p.howMany()

q = Person("q")
q.sayHello()
q.howMany()
