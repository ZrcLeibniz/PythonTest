# 推导式创建序列
# 推导式是一个或者多个迭代器快速创建序列的一种方法。
# 它可以将循环和条件判断相结合，从而避免冗余的代码
# 推导式是典型的Python风格，会使用它代表你已经入了Python的门

# 列表推导式
a = [x for x in range(1, 5)]
for x in range(len(a)):
    print(a[x], end='\t')
print()
b = [x * 2 for x in range(1, 5)]
for x in range(len(b)):
    print(b[x], end='\t')
    print()
c = [x for x in range(0, 51) if x % 5 == 0]
for x in range(len(c)):
    print(c[x], end='\t')
print()
d = [(row, col) for row in range(1, 10) for col in range(1, 10)]
print(d)

# 字典推导式
my_text = 'i love you , i love china , i love rich'
char_count = {e: my_text.count(e) for e in my_text}
print(char_count)

# 集合推导式
k = {x for x in range(1, 101) if x % 9 == 0}
print(k)

# 生成器推导式
gnt = (x for x in range(101) if x % 3 == 0)
w = tuple(gnt)
print(w)
