def fun01():
    l = [54, 36, 75, 28, 50]
    l.append(42)
    print("在列表尾部插入元素42: ", l)
    l.insert(l.index(28), 66)
    print("在28前面插入元素66: ", l)
    # popValue = l.remove(28)   要求输出删除的结果，不能使用remove
    popValue = l.pop(l.index(28))
    print("删除并输出元素28: ", popValue)
    l.sort()
    l.reverse()
    print("将列表按降序排序:", l)
    l.clear()
    print("清空整个列表:", l)


def fun02():
    lst_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lst_3 = []
    lst_3.append("abc")
    print("向列表lst_3中添加一个元素‘abc':", lst_3)
    ls_5 = list('efg')
    lst_3.extend(ls_5)
    # 通过切片的操作在前面插入lst_1序列
    lst_3[0:0] = lst_1
    print("将lst_5追加至尾部，lst_1插入最前面:", lst_3)
    lst_3.remove(3)
    lst_3.remove(4)
    lst_3.remove(5)
    print("删除3,4,5三个元素", lst_3)
    # lst_3.insert(0, 's')
    lst_3[0] = 's'
    print("在lst_3的最前面添加元素's':", lst_3)
    lst_3[0] = 'hello'
    print("将lst_3得到1号元素(0)替换为 'hello':", lst_3)


def fun03():
    nums = [3, 6, 10, 14, 2, 7]
    result = []
    for i in range(0, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == 9:
                result.append((nums[i], nums[j]))
    print(result)


def fun04():
    judgeCount = int(input("输入评委人数："))
    score = []
    for i in range(1, judgeCount + 1):
        score.append(int(input("输入第%d个评委打的分数:" % i)))

    score.remove(max(score))
    score.remove(min(score))
    print("去掉最高分和最低分的平均值为:%.2f" % (sum(score) / len(score)))


def fun05():
    while True:
        arr = list(map(int, input("输入任意奇数个整数，用逗号隔开:").split(',')))
        if len(arr) % 2 == 1:
            break
    arr.sort()
    print("arr的中间值为:%d" % (arr[(len(arr) // 2)]))
    print(arr)


def fun06():
    s = input("输入一个四则运算的表达式：")
    result = 0
    if 'x' in s:
        s = s.replace('x', '*')
    result = eval(s)
    print("%s=%d" % (s.replace('*', 'x'), result))


def fun07():
    ls = [['张三', 18, '郑州市'], ['李四', 19, '开封市'], ['王五', 20, '洛阳市'], ['赵六', 18, '许昌市']]
    result = []
    for item in ls:
        temp = [item[0], item[2]]
        result.append(temp)
    print(result)


def fun08():
    l, m = map(int, input('L,M:').split())
    arr = [1 for i in range(0, l)]
    area = []
    for i in range(1, m + 1):
        x1, x2 = map(int, input("输入区域的起始点和终止点的坐标：").split())
        area.append((x1, x2))

    for item in area:
        for i in range(item[0], item[1] + 1):
            arr[i] = 0
    print("马路上剩余的树的数目:%d" % (l - arr.count(0)))


def fun09():
    lst_1 = [10, 10, 6, 10, 10, 2, 10, 10, 10, 4, 10, 3, 10, 8, 10, 2, 10, 3, 10, 10]

    # lst_1 = [x for x in lst_1 if x != 10]

    result = []
    for item in lst_1:
        if item != 10:
            result.append(item)
    lst_1 = result

    print(lst_1)





