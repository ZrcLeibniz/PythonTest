# 测试_enumerate()函数和推导式生成列表

a = ['我 love u！\n', '张锐驰\n', '何丽雯\n']
b = enumerate(a)
print(a)
print(list(b))

with open(r"a.txt", 'r', encoding="UTF-8") as f:
    lines = f.readlines()
    lines = [temp + '#' + str(index) for index, temp in enumerate(lines)]
    print(lines)
