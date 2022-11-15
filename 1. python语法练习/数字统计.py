"""
    数字统计：统计1，2，3，4组成的无重复位数的三位数字的个数

    Version: 1.0
    Date: 2022-7-15
    Author: 靳靳靳
"""

count = 0
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if a != b and a != c and b != c:
                print("{0:>6}".format(a * 100 + b * 10 + c), end="")
                count += 1
    print(end="\n")

print("一共有：" + str(count) + "个数")
