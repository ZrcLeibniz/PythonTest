# 函数的学习
# python中，定义函数的语法为：
# def 函数名(参数列表)
#   '''文档字符串'''
#   函数体


def test01():
    print('*' * 10)
    print('@' * 10)


print(id(test01))
print(type(test01))
print(test01)


# for i in range(10):
# test01()

def printMax(a, b):
    """用于比较两个数的大小，并且返回较大的值"""
    if a < b:
        return b
    else:
        return a


def printAvg(a, b):
    return [a, b, (a + b) / 2]


help(printMax.__doc__)