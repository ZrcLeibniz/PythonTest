# 使用递归函数计算阶乘

import numpy


def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


a = factorial(3)
print(a)


a = numpy.arange(0, 60, 10).reshape(-1, 1)+numpy.arange(6)
print(a)
