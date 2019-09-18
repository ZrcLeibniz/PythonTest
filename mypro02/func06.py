# lambda表达式的学习
# 该表达式可以用来声明匿名函数。其实一种简单的，在同一行中定义函数的方法。
# lambda函数实际生成了一个函数对象
# lambda表达式只允许包含一个表达式，不能包括复杂语句，该表达式的计算结果就是函数的返回值


f = lambda a, b, c, d: a * b * c * d
print(f(1, 2, 3, 4))

g = [lambda a: a ** 2, lambda b: b ** 3, lambda c: c ** 4, lambda d: d ** 5]
print(g[0](6))
