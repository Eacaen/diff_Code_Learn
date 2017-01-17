class Fruit:
    def __init__(self):
        self.__color = "red"        # 定义私有变量

class Apple(Fruit):                 # Apple继承了Fruit
    “””This is doc”””               # doc文档
    pass
        
if __name__ == "__main__":
    fruit = Fruit()
    apple = Apple()
    print(Apple.__bases__ )         # 输出基类组成的元组
    print(apple.__dict__)           # 输出属性组成的字典
    print(apple.__module__)         # 输出类所在的模块名
    print( apple.__doc__)           # 输出doc文档
