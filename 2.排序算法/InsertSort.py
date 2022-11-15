"""
    插入排序，把数据分为有序和无序，从无序的部分拿出，插入到有序部分
"""
import time
from random import random
from time import struct_time

array = [int(random() * 80000) for i in range(0, 80000)]


def insertSort(arr: "需要排序的数组"):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            j = i - 1
            while j >= 0:
                if arr[j] > arr[j + 1]:
                    temp = arr[j]
                    arr[j] = arr[j + 1]
                    arr[j + 1] = temp
                j -= 1


localtime = time.localtime(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))
insertSort(array)
localtime = time.localtime(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))
