import pickle


class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


# stu = Student("小明", 15, "男")
# print(pickle.dumps(stu))    # dumps()函数会将对象序列化，并返回数据，而dunp()函数可以直接将对象序列化并写入文件对象中,文件参数是IO流

# stu = Student("小红", 16, "女")
# with open("object.data", "wb") as f:  # wb：以二进制格式打开文件写入
#     pickle.dump(stu, f)


with open("object.data", "rb") as f:
    stu = pickle.loads(f.read())
    print(isinstance(stu, Student))
