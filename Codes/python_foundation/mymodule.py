#!/usr/bin/python
# -*- coding:UTF-8 -*-
#Filename:backup_ver1.py

# 这个小脚本作用是把固定地址的文件压缩备份
# 主要看下os模块的用法
# time模块官方文档 http://docs.python.org/library/time

import os
import time

def mkdir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def makeupZipPath(comment):
    # 初始化文件夹路径
    target_dir = './backup/'
    today = target_dir + time.strftime('%Y%m%d')
    now = time.strftime('%H%M%S')
    # 检测并创建文件夹
    mkdir(target_dir)
    mkdir(today)
    # 拼接备份文件名 - os.sep - 分隔符，为了做跨平台
    if len(comment) == 0:
        target = today + os.sep + now + '.zip'
    else:
        target = today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'
    return target

def main():
    source = ['./1.gif','./2.gif']
    target = makeupZipPath(raw_input('Enter a comment -->'))

    zip_command = 'zip -qr %s %s' % (target,' '.join(source))

    if os.system(zip_command) == 0:
        print 'Successful backupt to', target
    else:
        print 'Backup FAILED'

if __name__ == '__main__':
    # 这个模块是主模块（不是被别的模块引入的）的时候执行
    main()
