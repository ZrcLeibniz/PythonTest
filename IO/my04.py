# 文本文件的读取
# read([size])函数：从文件中读取size个字符，并作为结果返回。
# readline()函数：读取一行文件作为结果返回。读取到文件末尾，会返回空字符串
# readlines()函数：文本文件中，每一行作为一个字符串存入列表中，返回该列表

with open(r"a.txt", 'r', encoding="UTF-8") as f:
    print(f.read(18))

with open(r'a.txt', 'r', encoding="UTF-8") as f:
    print(f.read())

with open(r"a.txt", 'r', encoding="UTF-8") as f:
    while True:
        fragment = f.readline()
        if not fragment:
            break
        else:
            print(fragment, end="")

with open(r"a.txt", 'r', encoding="UTF-8") as f:
    for a in f:
        print(a, end="")

with open(r"a.txt", 'r', encoding="UTF-8") as f:
    print(f.readlines())
