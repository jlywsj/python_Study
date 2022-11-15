# python中参数传递为基本数据类型时，为值传递
def exchange(v1: "variable one", v2: "variable two"):
    temp = v1
    v1 = v2
    v2 = temp
    print("v1 = %d, v2 = %d" % (v1, v2))


a = 1
b = 2

exchange(a, b)


# print("a = %d, b = %d" % (a, b))

# 如果传递的为对象类型，为引用传递
def addList(array: "list", arg: 'value'):
    array.append(arg)
    return 1


arr = [1, 2]
addList(arr, 12312)

# print(addList(arr, 12312))

# print("{b}{a}".format(a='a', b='b'))
# print("{1}{0}".format(a, b))


def sumNum(num1: "int", num2: "int") -> int:
    """ python中函数通过在后面加:指明参数类型，->指明返回值类型 """
    return num1 + num2


# Lambda函数
lam = lambda k, v: "%s=%d" % (k, v)

print(lam("a", 2))
