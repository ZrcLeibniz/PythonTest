# 递归的学习


# def test01(n):
#     print('test01', n)
#     if n == 0:
#         print('hahaha')
#     else:
#         test01(n - 1)
#     print('test01***', n)
#
#
# def test02():
#     test01()
#     print('test02')
#
#
# n = input("请输入数字：")
# test01(int(n))


def test03(n):
    if n == 1:
        return n
    else:
        return n * test03(n - 1)


print(test03(3))
