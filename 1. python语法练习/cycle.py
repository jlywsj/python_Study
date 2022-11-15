"""
for循环(for-in)的语法格式：
    for x in range(a,b,step)
循环变量x从a到b以step为步长依次增加。左闭右开

"""

from math import sqrt

# 输出100以内的偶数和
def even():
    sum = 0
    for x in range(2, 101, 2):
        sum += x
    print(sum)


# 输出一千以内的三位数水仙花数（各位数的立方的和为原来的数）
def water_flower():
    for x in range(100, 1000):
        a = x % 10  # 个位数
        b = x // 10 % 10  # 十位数
        c = x // 100  # 百位数
        count = 0
        if (a ** 3 + b ** 3 + c ** 3) == x:
            count += 1
            print(x, end="\t")


#    练习1：输入一个正整数判断是不是素数。
#    提示：素数指的是只能被1和自身整除的大于1的整数。

def prime_number():
    number = int(input("请输入一个数字："))
    end = int(sqrt(number))
    isPrime = 1
    for x in range(2, end + 1):
        if number % x == 0:
            isPrime = 0
            break
    if isPrime and number != 1:
        print("%d是素数" % number)
    else:
        print("%d不是素数" % number)

"""
    while循环语法格式：
        while boolean:
            循环体
    通常在不知道循环次数，但是知道循环结束条件的情况下使用while循环
"""


