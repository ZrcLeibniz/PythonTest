# Python在查找变量名时是按照LEGB规则查找的
# L:Local 函数或者类的内部
# E: Enclosed 嵌套函数
# G:Global 模块中的全局变量
# B:Build in Python保留的特殊名称
import numpy

str_1 = 'uni'


def outer():
    str_1 = 'outer'

    def inner():
        str = 'inner'
        print(str)

    inner()


outer()
