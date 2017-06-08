# -*- coding:UTF-8 -*-
#!/usr/bin/python

# 发生错误，Python默认使用错误处理器对错误进行处理：
# exit and print
# 使用try...except拦截异常并处理
# 使用raise引发异常

import sys

class ShortInputException(Exception):
    '''A user - defined exception class'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

def tryFunctionTest():
    try:
        s = raw_input('Enter something -->')
        if len(s) < 3:
            raise ShortInputException(len(s), 3)
    except EOFError:
        print '\nWhy did you do an EOF on me?'
        sys.exit()
    except ShortInputException, x:
        print 'ShortInputException: The input was of length %d, \
        was expecting at least %d' % (x.length, x.atleast)
    except:
        print '\nSome error /exception occurred.'
    else:
        print 'No exception was raise'
    print 'Done'

if __name__ == '__main__':
    tryFunctionTest()
