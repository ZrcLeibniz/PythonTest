# 字典的创建
a = {'name': 'rich', 'age': 21, 'job': 'programmer'}
b = dict(name='rich', age=21, job='programmer')
# 通过zip()方式进行字典的创建
k = ['name', 'age', 'job']
v = ['rich', 21, 'programmer']
c = dict(zip(k, v))
print(a)
print(b)
print(c)
# 通过fromkeys创建值为空的字典
d = dict.fromkeys(['name', 'age', 'job'])
print(d)