"""
    输出*构成金字塔
    Version: 1.0
    Author: 靳靳靳
    Date: 2022-7-15
"""

level = int(input("输入要建几层"))
for x in range(1, level*2, 2):
    print("{0:^{1}}".format("*" * x, level * 2))
