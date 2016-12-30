class Factory:                              # 工厂类
    def createFruit(self, fruit):               # 工厂方法
        if fruit == "apple":                   # 如果是apple则返回类Apple
            return Apple()           
        elif fruit == "banana":                # 如果是banana则返回类Banana
            return Banana()

class Fruit:
    def __str__(self):
        return "fruit"

class Apple(Fruit):
    def __str__(self):
        return "apple"

class Banana(Fruit):
    def __str__(self):
        return "banana"

if __name__ == "__main__":
    factory = Factory()
    print(factory.createFruit("apple")  )       # 创建apple对象
    print(factory.createFruit("banana"))        # 创建banana对象
