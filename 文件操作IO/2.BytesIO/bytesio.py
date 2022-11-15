"""
    IO模块提供了BytesIO函数实现对二进制数据的读取和写入操作
    同样也是在内存中进行读取，不需要写入硬盘
"""

import io

f = io.BytesIO()
f.write("你好".encode("utf-8"))  # 通过encode()函数对字符串按指定字符集进行编码，此处写入的是经过utf-8编码的bytes
print(f.getvalue())  # 此处获取的是经过utf-8编码的数据
print(f.getvalue().decode("utf-8"))  # encode():编码， decode():解码  用"utf-8"编码进行解码

f = io.BytesIO("中文".encode("utf-8"))
print(f.read().decode("utf-8"))
