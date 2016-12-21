class Fruit:
    def __init__(self, color):         # 初始化属性__color
        self.__color = color
        print(self.__color)
    
    def getColor(self):
        print(self.__color) 
    
    def setColor(self, color):
        self.__color = color
        print(self.__colo)r

if __name__ == "__main__":
    color = "red"
    fruit = Fruit(color)                # 带参数的构造函数
    fruit.getColor()
    fruit.setColor("blue")
