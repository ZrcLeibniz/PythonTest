# 测试全局变量和局部变量
# 如果要在函数内部使用全局变量要使用global声明

a = 3


def test01():
    global a
    a = 300
    b = 4
    print(a)
    print(b)


print(a)
test01()

print()
