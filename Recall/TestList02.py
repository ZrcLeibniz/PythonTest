# 列表元素的增加和删除


# append()方法
a = [20, 40]
print(a)
print(id(a))
a.append('rich')
print(a)
print(id(a))

# “+”运算符操作
# 通过输出b对象的地址发现，此方法生成了新的对象所以一般情况下尽量不要使用
b = [20, 40]
print(b)
print(id(b))
b = b + ['rich']
print(b)
print(id(b))

# extends()方法
# 并没有生成新的对象,一般进行列表整合时推荐使用此方法
c = [20, 40]
print(id(c))
print(c)
c.extend([50, 60])
print(c)
print(id(c))

# insert()插入方法
d = [10, 20, 30]
d.insert(1, 15)
print(d)

# 乘法扩展
a = ['rich', 100]
b = a * 3
print(b)
