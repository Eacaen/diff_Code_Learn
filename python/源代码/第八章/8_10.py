class Fruit:                                         # 基类
    def __init__(self, color):
        self.color = color
        print("fruit's color : %s" % self.color)

    def grow(self):
        print("grow ...")

class Apple(Fruit):                                  # 继承了Fruit类
    def __init__(self, color):                         # 子类的构造函数
        Fruit.__init__(self, color)                    # 显式调用父类的构造函数
        print("apple's color : %s" % self.color)

class Banana(Fruit):                                # 继承Fruit类
    def __init__(self, color):                         # 子类的构造函数
        Fruit.__init__(self, color)                    # 显式调用父类的构造函数
        print("banana's color : %s" % self.color)

    def grow(self):
        print("banana grow ...")

if __name__ == "__main__":
    apple = Apple("red")
    apple.grow()                       # 调用grow方法
    banana = Banana("yellow")
    banana.grow()                     # 调用grow方法
