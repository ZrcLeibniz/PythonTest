# 二进制文件的读取和写入

with open("LiWenHe.jpg", 'rb') as f:
    with open("HeLiWen.jpg", 'wb') as g:
        for line in f.readlines():
            g.write(line)
print("图片拷贝完成")