# break的学习
# break可用于while和for循环，用来结束整个循环。当有嵌套循环时，break语句只能跳出最近一层循环
# continue的学习
# continue语句用于结束本次循环，继续下一次循环。多个循环嵌套时，continue也是应用于最近一层循环
while True:
    a = input("请输入一个字符：")
    if a == 'q' or a == 'Q':
        print('循环结束，退出')
        break
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')

empNum = 0
salary = []
salarySum = 0
while True:
    s = input("请输入员工的薪资：（按q或者Q结束录入）")
    if s == 'q' or s == 'Q':
        print('录入结束')
        break
    if float(s) < 0:
        print('请认真输入员工薪资')
        continue
    empNum = empNum + 1
    salary.append(float(s))
    salarySum = salarySum + float(s)
    print("共有工人:{0}".format(empNum))
    print("录入薪资:", salary)
    print("平均薪资为：{0}".format(salarySum/empNum))
