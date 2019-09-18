# 嵌套循环的学习
for x in range(5):
    for y in range(5):
        print(x, end='\t')
    print()

print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

for x in range(1, 10):
    for y in range(1, x + 1):
        print('{0}*{1}={2}'.format(x, y, (x * y)), end='\t')
    print()
