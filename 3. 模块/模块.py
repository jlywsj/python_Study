import math  # 引入一个模块
# 从包中引入模块
from package1 import hello1 as h1
from package1 import hello2 as h2

h1.sayHello()
h2.sayNight()

# 需要用到模块中的函数或变量的时候通过 模块名.函数名 来调用
print(math.pow(2, 3))

# import
# import turtle, time, math  # 使用import 引入多个模块
