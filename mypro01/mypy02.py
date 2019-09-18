# 测试双分支选择结构
num = input("请输入一个数字：")
if int(num) < 10:
    print("num时小于10的数字")
else:
    print("num时大于10的数字")

# 测试三元运算符
num2 = input("请输入一个数字：")
print(num2 if(int(num2) > 10) else "数字太大")
