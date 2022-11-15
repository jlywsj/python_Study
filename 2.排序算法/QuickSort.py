"""
    快速排序：取一个中间大小的数字作为基准，将比该数字大的放在右边，小的放在左边
        通过分治的思想，对两边的数据进行递归调用
"""
import time
from random import random
import sys

# 设置递归深度
# sys.setrecursionlimit(1000000)

array = [int(random() * 80000) for i in range(0, 80000)]


def quickSort(arr, left, right):
    pivot = arr[(left + right) // 2]
    l = left
    r = right

    while l < r:
        while arr[l] < pivot:
            l += 1

        while arr[r] > pivot:
            r -= 1

        if l >= r:
            break

        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp

        # 如果有一边已经遍历到pivot，而另一边还没有到
        if arr[l] == pivot:
            r -= 1
        if arr[r] == pivot:
            l += 1

    if l == r:
        l += 1
        r -= 1

    if left < r:
        # 尾递归是指，在函数返回的时候，调用自身本身，
        # 并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，
        # 使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
        return quickSort(arr, 0, r)

    if right > l:
        # 递归调用是函数调用自己，在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
        # 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。9+
        # 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。
        return quickSort(arr, l, len(arr) - 1)


localtime = time.localtime(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))

quickSort(array, 0, len(array) - 1)

localtime = time.localtime(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))
