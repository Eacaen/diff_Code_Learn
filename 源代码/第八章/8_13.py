class Fruit:                                     # 父类
    def __init__(self):
        pass

class HuskedFruit(Fruit):                           # 削皮水果
    def __init__(self):
        print("initialize HuskedFruit")
    
    def husk(self):                                 # 削皮方法
        print("husk ...")

class DecorticatedFruit(Fruit):                     # 剥皮水果
    def __init__(self):
        print("initialize DecorticatedFruit")

    def decorticat(self):                           # 剥皮方法
        print("decorticat ...")

class Apple(HuskedFruit):
    pass

class Banana(DecorticatedFruit):
   pass
