# 嵌套函数的学习
# 在函数内部定义的函数
# 如果外部函数需要使用外部函数的局部变量，需要使用nonlocal啦声明


def f1():
    print('outer running')

    def f2():
        print('inner running')

    f2()


f1()


def printName(isChinese, name, familyName):
    def inner_print(a, b):
        print("{0} {1}".format(a, b))

    if isChinese:
        inner_print(familyName, name)
    else:
        inner_print(name, familyName)
