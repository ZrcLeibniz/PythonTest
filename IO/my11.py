# coding=utf-8
# 测试os模块中，关于文件和目录的操作

import os
# 获取文件和文件夹相关的信息
print(os.name)  # windows->nt, linux和unix->posix
print(os.sep)  # windows->\, linux和unix->/
print(repr(os.linesep))  # windows->\r\n, linux和unix->\n\
print(os.stat("my11.py"))  # 获取文件信息

# 关于工作目录的操作
print(os.getcwd())
os.chdir("D:")
os.mkdir("书籍")
os.rmdir("书籍")
os.makedirs('电影/港台/周星驰')
os.removedirs('电影/港台/周星驰')
os.rename('dianying', 'movie')
dirs = os.listdir('movie')
print(dirs)

# 创建目录、多级目录、删除目录
