# -*- coding:UTF-8 -*-
#!/usr/bin/python

# 这里对Python的知识做下补充

def specified_functions():
    # 特殊方法
    # 一般来说，特殊方法都会被用来模仿某个行为
    # 如，希望你的类使用x[key]这种操作，需要实现__getitem__()方法
    # 类比下iOS的description方法..
    '''
    __init__(self): init方法
    __del__(self): deloc方法
    __str__(self): description方法
    __It__(self,other): < 运算符调用的方法
    __getitem__(self,key): x[key]
    __len__(self)
    '''

def singleSentence():
    # 单语句块
    if True: print 'YES'

def functionalOperaction():
    # 列表综合 - 看着像函数式的操作...
    listone = [2,3,4]
    listtwo = [2 * i for i in listone if i > 2]
    print listtwo

def tupleArgv(*args):
    # 元组作为参数 - *args
    # 字典作为参数 - **args

def lambdaSentence():
    # 用来创建新函数，并在运行时返回它们
    def make_repeatr(n):
        return lambda s: s*n

    twice = make_repeatr(2)

    print twice('word') # wordword
    print twice(5) # 10

def execAndEval():
    # exec - 执行存储在字符串中的命令
    # eval - 计算存储在字符串中的Python表达式
    eval('2*3')
def assertSentence():
    # 断言
    assert True
