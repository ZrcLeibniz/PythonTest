# 切片操作
# 三个参数[起始偏移量:终偏移量:步长]

a = [10, 20, 30, 40, 50, 60]
print(a[:])
print(a[1:])
print(a[:4])
print(a[1::2])
print(a[::2])
for x in a:
    print(x)