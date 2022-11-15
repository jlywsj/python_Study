# f = open("a.txt", "r", encoding="utf-8")    # oepn的参数: 1.文件 2. 打开方式 3. 读写编码
# text="utf-8写入"
# print(f.write(text))

from datetime import datetime

f = open(file="a.txt", mode="a", encoding="utf-8")  # mode: r:读 w:写 a:在尾部追加
now = str(datetime.now()) + "\n"
print(f.write(now))
