# 生成器推导式创建元组
s = (x*2 for x in range(5))
print(s)
a = tuple(s)
print(a)
