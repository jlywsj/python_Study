
"""
    用户登录时，验证密码输入是否正确账号为root 密码为 admin

    Version: 1.0
    Auther: 靳靳靳
    Date: 2022-7-15
"""

isTrue = 0

for i in range(3):
    name = input("username:")
    password = input("password:")
    if name == "root" and password == "admin":
        isTrue = 1
        break
    else:
        print("密码错误，你还有"+str(2-i)+"次机会")
if isTrue:
    print("登录成功！")
else:
    print("登录失败！")
