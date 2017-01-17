class Student:                          # 类名大写
    __name = ""                         # 私有实例变量前必须有两个下划线
    def __init__(self, name):
        self.__name = name              # self相当于Java中的this

    def getName(self):                  # 方法名首字母小写，其后每个单词的首字母大写
        return self.__name
  
    if __name__ == "__main__":
        student = Student("borphi")     # 对象名小写
        print(student.getName())
