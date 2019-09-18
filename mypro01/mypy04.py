# 选择结构的嵌套
score = int(input("请输入学生的分数："))
grade = ''
if score > 100 or score < 0:
    print("请认真输入学生的分数")
    score = int(input("请输入学生的分数："))
else:
    if 0 <= score < 60:
        grade = "不及格"
    elif 60 <= score < 80:
        grade = "及格"
    elif 80 <= score < 90:
        grade = "良好"
    elif 90 <= score <= 100:
        grade = "优秀"
    print("分数是{0},等级是{1}".format(score, grade))
