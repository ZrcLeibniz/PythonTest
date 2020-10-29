# coding=utf-8
# os.path模块的学习
# 此模块提供了目录相关的操作，例如:路径判断、路径切分、路径链接、文件夹遍历等等

import os
import os.path as osp

osp.isabs()  # 判断该路径是不是绝对路径
osp.isdir   # 判断该路径是不是目录
osp.isfile()  # 判断该路径是不是文件
osp.exists()    # 判断该路径所指文件是否存在
osp.getsize()   # 获取文件的基本信息，返回文件的大小
osp.abspath()    # 获取文件的绝对路径
osp.dirname()   # 获取文件的目录名称
osp.getctime()  # 获取文件的创建时间
osp.getatime()  # 获取文件的最后访问时间
osp.getmtime()  # 获取文件的最后修改时间
