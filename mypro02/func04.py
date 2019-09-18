# 学习浅拷贝和深拷贝
# 浅拷贝（copy）：不拷贝子对象的内容，只拷贝子对象的引用
# 深拷贝（deepcopy）：会连同子对象的内存也全部拷贝一份，对子对象的修改不会影响源对象


import copy


def testCopy():
    a = [10, 20, [5, 6]]
    b = copy.copy(a)
    print(a)
    print(b)
    b.append(30)
    b[2].append(7)
    print('浅拷贝')
    print(a)
    print(b)


def testDeepCopy():
    a = [10, 20, [5, 6]]
    b = copy.deepcopy(a)
    print(a)
    print(b)
    b.append(30)
    b[2].append(7)
    print('深拷贝')
    print(a)
    print(b)


testCopy()
print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
testDeepCopy()
