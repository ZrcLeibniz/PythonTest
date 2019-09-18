# 列表的创建


a = [10, 20, 'rich', 'excellent']
print(a)

b = list()
b.append(10)
b.append('rich')
print(b)

c = list(range(10))
print(c)

d = list('rich,is,excellent')
print(d)

e = range(10)
f = list(e)
print(f)


# 通过range创建整数列表
# 三个参数：start：表示其实数字；end：表示结尾数字；step：表示步长
g = list(range(12, 34, 3))
print(g)

h = list(range(10, 2, -1))
print(h)

# 推导式创建列表
i = [x*2 for x in range(5)]
print(i)

j = [x*2 for x in range(100) if x % 9 == 0]
print(j)