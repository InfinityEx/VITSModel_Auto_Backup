#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys
import os

# 扫描间隔
scan_interval=10

# 扫描路径及备份路径
scan_path='D:/Applications/GitProject/checkpoints'
bak_path='D:/Applications/GitProject/bakup'

# 保存上限
save_count=3

# 是否保存D_*.pth (0为不保存，1为保存，默认1)
Dfile_sav=1

def dircheck():
    a,b="",""
    err=0
    if not (os.path.exists(bak_path)):
        os.makedirs(bak_path)
        a='备份目录不存在，已自动创建'
    else:
        a='备份目录正常'
    if not (os.path.exists(scan_path)):
        b='模型保存路径不存在！请检查配置'
        err=1
    else:
        b='模型保存路径正常'
    print(f'模型保存路径检查：{b}\n备份路径检查：{a}')
    return err


if __name__ == "__main__":
    rdc=dircheck()
    if rdc==1:
        sys.exit(0)
    n=0
    if save_count==0:
        while 1:
            print('Saved')
    else:
        while(n<=save_count):
            print('Saved')
