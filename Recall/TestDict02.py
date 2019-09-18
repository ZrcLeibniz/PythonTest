# 字典元素的访问
a = dict(name='rich', age='21', job='programmer')
print(a['name'])
b = a.get('age')
print(b)
# 列出所有的键值对
c = a.items()
print(c)
# 列出所有的键
d = a.keys()
print(d)
# 列出所有的值
e = a.values()
print(e)
# 获得键值对的个数
f = len(a)
print(f)
# 检测一个键是否在字典中
print('name' in a)

