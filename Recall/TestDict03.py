# 字典元素的添加，修改和删除
# 给字典新增键值对，如果键已经存在，则覆盖旧的键值对
a = dict(name='rich', age='21', job='programmer')
a['address'] = '陕西'
print(a)
# 使用update()将新字典中的键值对全部添加都老键值对上，如果重复，直接覆盖
b = {'name': 'rich2', 'money': '1000'}
a.update(b)
print(a)
# 字典中元素的删除可以使用del();使用clear()删除所有键值对;pop()删除指定键值对,并返回'值对象'
del(a['name'])
print(a)
b = a.pop('age')
print(b)
# popitem()随机的删除和返回键值对。
a.popitem()
print(a)

