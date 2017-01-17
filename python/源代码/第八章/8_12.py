class Fruit:
    def __init__(self):
        print("initialize Fruit")
    
    def grow(self):                             # 定义grow()方法
        print ("grow ...")

class Vegetable(object):
    def __init__(self):
        print("initialize Vegetable")    

    def plant(self):                              # 定义plant方法
        print("plant ...")

class Watermelon(Vegetable, Fruit):             # 多重继承，同时继承Vegetable和Fruit
    pass

if __name__ == "__main__":
    w = Watermelon()            # 多重继承的子类，拥有父类的一切公有属性
    w.grow()
    w.plant()
