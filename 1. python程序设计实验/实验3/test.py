# 1
def fun01():
    # 建国：1949   建党：1921
    year = int(input('输入一个年份：'))
    if year < 0:
        print("illegal year")
    else:
        if (year - 1921) % 10 == 0:
            print("Good year")
        elif (year - 1949) % 10 == 0:
            print("Lucky year")
        else:
            print("Common year")


# 2
def fun02():
    """定义一个正方形的四个角 rightTop, rightBottom, leftBottom, leftTop"""
    arr = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    x, y = int(input("输入点的x坐标：")), int(input('输入点的y坐标：'))
    if arr[2][0] <= x <= arr[0][0] or arr[2][1] <= y <= arr[0][1]:
        print("该点在正方形内部")
    else:
        print("该点在正方形外面")


# 3
def fun03():
    pm = int(input("请输入空气中PM2.5的数值："))
    s = ""
    if pm > 75:
        s = "污染严重"
    elif pm >= 35:
        s = "良好"
    else:
        s = "优"
    print("今日空气质量%s" % s)


# 4
def fun04():
    x = int(input("输入一个整数x,将返回函数值y:"))
    y = 0
    if 5 <= x < 10:
        y = 5 * x - 25
    if 10 <= x:
        y = (x - 5) ** 2
    print("y=%d" % y)


# 5
def fun05():
    num = eval(input("输入一个整数："))
    if num % 2 == 0 and num % 3 == 0:
        print("Yes")
    else:
        print("No")
    print(num)


# 6
def fun06():
    from math import sqrt
    MAXSIZE = 10000
    for i in range(-100, MAXSIZE):
        x = i + 100
        if int(sqrt(x)) ** 2 == x and int(sqrt(x + 168)) ** 2 == x + 168:
            print(i)


# 7
def fun07(i):
    s = 0
    for n in range(1, i + 1):
        s += (-1) ** (n + 1) / (2 * n - 1)
    return 4 * s


# 8
def fun08():
    # 设 大中小马 a,b,c 匹
    a = 0
    b = 0
    c = 0
    for a in range(0, 33):
        for b in range(0, 50):
            for c in range(0, 100):
                if a + b + c == 100 and 3 * a + 2 * b + c // 2 == 100:
                    print("大马%d匹\t中马%d匹\t小马%d匹" % (a, b, c))


# 9
def fun09():
    x = int(input("输入层数x:"))
    maxCount = 2 * x - 1
    for i in range(1, x + 1):
        # 打印空白
        count = 2 * i - 1
        for j in range(0, (maxCount - count) // 2):
            print(" ", end="")
        # 打印 *
        for k in range(0, count):
            print("*", end="")
        print()


# 10
def fun10(n):
    # count = n
    # chars = 2 * n + 1
    for i in range(1, n + 1):
        # 每一层最前面的空格为当前的层数
        # 打印空格
        for j in range(0, i):
            print(" ", end="")
        # 打印数字
        # 第一层 n + 1 - i 个数，从1开始
        for k in range(1, n + 1 - i + 1):
            print("%d " % k, end="")
        print()


# 11
def fun11():
    # 每一行的表达式个数都是从 行号 到 9,前面是十个空白 6 + \t,空白看 行号-1
    for i in range(1, 10):  # 行
        # 打印空白，每行打印一次
        for k in range(0, i - 1):
            print("        ", end="")
        for j in range(i, 10):  # 列
            # 打印乘法表
            print("%dx%d=%2d" % (i, j, i * j), end="\t")
        print()


# 12
def fun12():
    def check(array, *args):
        for item in args:
            if not (item in array):
                return False
        return True

    count = 0
    arr = [1, 2, 3, 4]
    for i in range(100, 1000):
        a = i % 10
        b = i // 10 % 10
        c = i // 100
        if check(arr, a, b, c) and a != b != c and a != c:
            print("%d\t" % i, end="\t")
            count += 1
        if count == 4:
            break


# 13
def fun13():
    a = 0.08
    n = 0
    while True:
        n += 1
        if a * (2 ** n) > 8848.13:
            print("对折%d次" % n)
            break


