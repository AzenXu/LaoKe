#!/usr/bin/python
# -*- coding:UTF-8 -*-
# 这个文件来看看输入输出

# 储存器 - Python 的 pickle模块，可以持久化对象... cPickle比pickle快一点

import cPickle as p

def poemOutput():
    poem = '''\
    锄禾日当午，汗滴禾下土。
    谁知盘中餐，粒粒皆辛苦。
    '''
    f = file('poem.txt', mode='w')
    f.write(poem)
    f.close()

def poemFileRead():
    f = file('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0: # 读到了EOF
            break
        print line, # 加,可以去掉末尾换行符
    f.close()

shopListFile = 'shop_list.data'

def objectOutput():
    shopList = ['apple', 'mango', 'carrot']

    f = file(shopListFile, mode="w")
    p.dump(shopList, f) # 把对象dump出去
    f.close()

    del shopList

def objectFileLoad():
    f = file(shopListFile)
    storedList = p.load(f)
    print storedList

def main():
    poemOutput()
    poemFileRead()

    objectOutput()
    objectFileLoad()

if __name__ == '__main__':
    main()
