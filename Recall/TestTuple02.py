# 元组元素的访问和计数
a = (20, 30, 40, 50)
print(a[2])
print(a[0:2:1])
# 对于元组而言内部没有排序方法，只能使用内部函数sorted(tupleObj)，并且产生新的列表对象
a = (10, 20, 30, 9, 8)
b = sorted(a)
print(b)
# 可以通过zip函数，将多个列表组合成元组，并且返回这个zip对象
a = [10, 20, 30]
b = [40, 50, 60]
c = [70, 80, 90]
d = zip(a, b, c)
print(d)
e = list(d)
print(e)