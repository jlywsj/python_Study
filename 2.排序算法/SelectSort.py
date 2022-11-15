"""
    选择排序：依次选择所有数据中值最小的，放到最前面
"""

import time

# array = [9, 6, 7, 4, 3, 7, 2, 0]

array = [item for item in range(80000, 0, -1)]
print(len(array))


def selectSort(arr: "Array to sort"):
    for i in range(0, len(arr)):
        temp = arr[i]
        index = i
        for j in range(i, len(arr)):
            if arr[j] < temp:
                temp = arr[j]
                index = j
        arr[index] = arr[i]
        arr[i] = temp


localtime = time.localtime(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))
selectSort(array)
localtime = time.localtime(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))
