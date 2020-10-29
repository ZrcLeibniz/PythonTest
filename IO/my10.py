# os和os.path模块
# os模块可以帮助我们直接对操作系统进行操作。
# 可以直接调用操作系统的可执行文件、命令、直接操作文件、目录等等。

# os调用操作系统文件和命令
# os.system可以帮助我们直接调用系统的命令

import os
os.system("notepad.exe")
os.system("ping www.baidu.com")
os.system("cmd")

# 直接调用可执行的程序
os.startfile(r"要执行程序的绝对路径")