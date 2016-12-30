class Fruit:
    price = 0                                   # 类变量

    def __init__(self):
        self.__color = "red"                      # 定义私有变量

    def getColor(self):
        print(self.__color)                       # 打印私有变量
    
    @ staticmethod                              # 使用@staticmethod修饰器静态方法
    def getPrice():
        print(Fruit.price)

    def __getPrice():                            # 定义私有函数
        Fruit.price = Fruit.price + 10
        print(Fruit.price)
    
    count = staticmethod(__getPrice)                # 使用staticmethod方法定义静态方法

if __name__ == "__main__":
    apple = Fruit()                              # 实例化apple
    apple.getColor()                            # 使用实例调用静态方法
    Fruit.count()                                # 使用类名调用静态方法
    banana = Fruit()
    Fruit.count()
    Fruit.getPrice()
