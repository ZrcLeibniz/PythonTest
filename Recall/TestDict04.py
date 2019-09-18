# 序列解包
x, y, z = (10, 20, 30)
print(x, y, z)
(a, b, c) = (10, 20, 30)
print(a, b, c)

# 序列解包用于字典时，默认是对“键”进行操作；如果要对值进行解包，则需要使用values()
s = {'name': 'rich', 'age': 21, 'salary': 10000}
w, e, r = s
print(w, e, r)
t, h, k = s.values()
print(t, h, k)
d, q, l = s.items()
print(d, q, l)
