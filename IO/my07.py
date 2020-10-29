# 文件对象的常用属性和方法
# 文件对象的属性
# name 返回文件的名字 mode 返回文件的打开模式 closed 若文件被关闭则返回True
# 文件对象的打开方式
# r 读模式 w 写模式 a 追加模式 b 二进制模式（可以其他模式组合） + 读写模式（可以其他模式组合）
# 文件对象常用方法
# read([size]) 从文件中读取size个字节或字符的内容返回，若省略size，则读取全部
# readline() 从文本文件中读取一行内容
# readlines() 把文本中的每一行都作为独立的字符串对象，并将这些对象放入列表返回
# write(str) 把字符串str内容写入文件
# writelines(s) 把字符串列表s写入问津，不添加换行符
# seek(off/set[, whence])
# 把文件指针移动到新的位置，offset表示相对于whence的多少个字节的偏移量
# off/set off为正往结束方向移动， set为负往结束方向移动
# 0表示从文件头开始计算
# 1表示从当前位置开始计算
# 2表示从文件尾开始计算
# tell() 返回当前文件指针的位置
# truncate([size]) 无论指针在什么位置，只留下指针前size个字节的内容，其余全部删除
# 如果没有传入size，则将指针当前位置到文件末尾内容全部删除
# flush() 把缓冲区的内容写入文件但是不关闭文件
# close() 把缓冲区内容写入文件，同时关闭文件，释放文件对象相关资源

with open(r'a.txt', 'r', encoding="UTF-8") as f:
    print("文件名是：{0}".format(f.name))
    print(f.tell())
    print("读取的内容是：{0}".format(f.read()))