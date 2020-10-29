# CSV文件的操作
import csv
# with open("data.csv", "r") as f:
#     data_csv = csv.reader(f)
#     print(data_csv)
#     # print(list(data_csv))
#     for row in data_csv:
#         print(row)

with open("data_2.csv", 'a') as g:
    b_csv = csv.writer(g)
    b_csv.writerow(["ID", "姓名", "年龄"])
    data = [["zrc", "zrc", "zrc"], ["zrc", "zrc", "zrc"], ["zrc", "zrc", "zrc"]]
    b_csv.writerows(data)
