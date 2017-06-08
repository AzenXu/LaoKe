# -*- coding:UTF-8 -*-
#!/usr/bin/python

# 这个文件主要学习下sys模块和os模块

import sys # 包含系统对应的功能
import os # 包含普通的操作系统功能 - 如果希望跨平台，这个模块很重要

def readfile(filename):
    '''Print a file to the standard output'''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,
    f.close()

def osShow():
    print os.name # 正在使用的平台
    print os.getcwd() # 当前工作目录
    os.getenv() # 读取环境变量
    # os.putenv(key, value) #设置环境变量
    # os.listdir() # 返回指定目录下所有文件和目录名
    # os.remove() # 删除文件
    # os.system() # 运行shell命令
    # os.linesep # 终止符
    # os.path.split() # 用一个元组返回一个路径的目录名和文件名
    # os.path.isfile() os.path.isdir() 检测当前path是文件还是dir
    # os.exists() 检测路径是否存在

def testForSys():
    if len(sys.argv) < 2:
        print 'No action specified.'
        sys.exit()

        if sys.argv[1].startswith('-'):
            option = sys.argv[1][2:] # 取第一个参数的前两个字符 - 切片
            if option == 'version':
                print 'Version 1.2'
            elif option == 'help':
                print ''' 这里是 帮助 '''
            else:
                print 'Unknow option'
                sys.exit()
        else:
            for filename in sys.argv[1:]:
                readfile(filename)

if __name__ == '__main__':
    testForSys()
