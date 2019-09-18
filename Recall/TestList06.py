# 列表排序


# 修改原列表，不创建新列表的排序
a = [20, 10, 40, 30]
print(id(a))
# 将列表升序排列
a.sort()
print(a)
print(id(a))
# 将列表降序排列
a.sort(reverse=True)
print(a)

# 打乱顺序
import random
random.shuffle(a)
print(a)

print('__________________________________________')

# 创建新的列表的排序
b = [20, 10, 30, 40]
c = sorted(b)
print(c)

# reversed()返回迭代器
a = [10, 20, 30, 40]
c = reversed(a)
print(list(c))
