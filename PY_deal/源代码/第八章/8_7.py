class Fruit:
    def __init__(self, color):          # 初始化属性__color
        self.__color = color
        print(self.__color)

    def __del__(self):                  # 析构函数
        self.__color = ""
        print ("free ...")

    def grow(self):
        print("grow ...")

if __name__ == "__main__":
    color = "red"
    fruit = Fruit(color)                    # 带参数的构造函数
    fruit.grow()
