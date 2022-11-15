"""
    冒牌排序，通过依次比较两个数，将大的放在后面小的放在前面，通过不断循
    达到排序目的
"""

import time
import random

array = [0] * 80000

for i in range(0, 80000):
    array[i] = int(random.random() * 80000)

# print("%d-%d-%d %d:%d:%d" % (
#     localtime.tm_year, localtime.tm_mon, localtime.tm_mday, localtime.tm_hour, localtime.tm_min, localtime.tm_sec))
strT = "%Y-%m-%d %H:%M:%S"


def bubbleSort(arr):
    for i in range(0, len(arr)):
        # 添加判断，优化算法
        flag = False
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                flag = True
        if not flag:
            break


localtime = time.localtime(time.time())
print(time.strftime(strT, localtime))

listA = [3, 2, 1, 8, 9]
bubbleSort(listA)
# bubbleSort(array)
localtime = time.localtime(time.time())
print(time.strftime(strT, localtime))
print(listA)
