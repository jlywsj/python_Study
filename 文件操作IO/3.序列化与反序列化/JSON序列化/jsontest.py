import json
import jsonlines

"""
    JSON是一种轻量级的数据交换格式，
    json模块在python中只能序列化部分类型：
        dict, list, str, int, float, True, False, None
    不能序列化自定义的类对象
"""


class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


stu1 = {
    "name": "小明",
    "age": 18,
    "gender": "男"
}

stu2 = {
    "name": "小红",
    "age": 18,
    "gender": "女"
}

with open("student.json", "w") as f:
    json.dump(stu1, f)
    f.write("\n")
    json.dump(stu2, f)

with open("student.json", "r") as f:
    for item in jsonlines.Reader(f):
        print(item)
