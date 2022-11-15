"""
    希尔排序：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序
"""

# array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
import time
from random import random

array = [random() * 80000 for i in range(0, 80000)]


def shellSort(arr: "需要排序的列表"):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            j = i - gap
            while j >= 0:
                if arr[j] > arr[j + gap]:
                    temp = arr[j]
                    arr[j] = arr[j + gap]
                    arr[j + gap] = temp
                j -= gap
        gap //= 2


localtime = time.localtime(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))
shellSort(array)
localtime = time.localtime(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))
