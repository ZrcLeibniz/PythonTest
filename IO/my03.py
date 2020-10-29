s = ['\n张锐驰\n', '何丽雯\n']
with open(r"a.txt", 'a', encoding='UTF-8') as f:
    f.writelines(s)
