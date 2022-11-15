# f = open("a.txt", encoding="utf-8")
# text = f.read(8)
# print(text)

# 按行读文件
f = open(file="a.txt", mode="r", encoding="utf-8")

print(f.readline())
print(f.readline())
