# for循环的学习
for x in (10, 20, 30):
    print(x * 30)

for x in 'abcdefg':
    print(x)

a = ['姓名', '年龄', '薪资']
b = ['rich', 18, 200000]
z = dict(zip(a, b))
for x in z.keys():
    print(x)

for x in z.values():
    print(x)

for x in z.items():
    print(x)

print("#################################")

sum_all = 0
sum_even = 0
sum_odd = 0
for x in range(101):
    sum_all = sum_all + x
    if x % 2 == 0:
        sum_even = sum_even + x
    else:
        sum_odd = sum_odd + x
print("总和是：{0}，奇数和是：{1}，偶数和是：{2}".format(sum_all, sum_odd, sum_even))
