# 测试多分支选择结构
score = input("请输入学生的分数：")
if int(score) < 0 or int(score) > 100:
    print("请认真输入分数")
elif 90 <= int(score) <= 100:
    print("优秀")
elif 80 <= int(score) <= 89:
    print("良好")
elif 60 <= int(score) <= 79:
    print("及格")
elif 60 > int(score):
    print("不及格")
