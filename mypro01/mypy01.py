# 测试if语句(单分支选择结构)
num = input("请输入一个数字:")
if int(num) > 10:
    print('hello python')
else:
    print("Bye")

# 测试各种条件表达式
if 3:
    print("ok")

a = []
if a:
    print("false,空列表")

s = 'false'
if s:
    print("true")

c = 9
if 3 < c < 20:
    print("ok")

if 3 < c < 20:
    print("ok")

if True:
    print("ok")
