# 使用pickle序列化
# 序列化：将对象转化成“串行化”数据格式，存储到硬盘或通过网络传输到其他地方。

import pickle

# 将对象序列化到文件中
with open(r"file.dat", "ab") as f:
    a1 = "张锐驰"
    a2 = "234"
    a3 = [20, 30, 40]
    pickle.dump(a1, f)
    pickle.dump(a2, f)
    pickle.dump(a3, f)
