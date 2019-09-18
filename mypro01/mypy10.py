# 测试zip()并行迭代

for i in [1, 2, 3]:
    print(i)

names = ('rich', 'rich2', 'rich3', 'rich4')
ages = (18, 16, 21, 43)
jobs = ('老师', '程序员', '公务员')
for names, ages, jobs in zip(names, ages, jobs):
    print("{0}---{1}---{2}".format(names, ages, jobs))
