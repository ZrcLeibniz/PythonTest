# 集合的创建和删除
a = {3, 5, 7}
a.add(9)
print(a)
b = ['a', 'b', 'c', 'd']
c = set(b)
print(c)

k = {1, 3, 'rich'}
v = {'he', 'it', 'rich'}
# 集合的并集
h = k & v  # h = a.union(b)
# 集合的交集
j = k - v  # j = k.intersection(v)
# 集合的差集
o = k | v  # o = k.difference(v)
print(h)
print(j)
print(o)
