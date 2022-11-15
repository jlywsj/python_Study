from io import StringIO
"""
    使用StringIO实现在内存中读取和写入，并不需要真正地写入到文件中
    IO模块提供了对str操作的StringIO函数
"""
f = StringIO()
f.write('hello')
f.write('  ')
f.write('world!')
print("写入StringIO后的值："+f.getvalue()) # getvalue()用于获取写入后的str

f = StringIO("   Hello!\nWorld!\nWelcome!")
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip()) # strip() 去除字符串两端的空字符

