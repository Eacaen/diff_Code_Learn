tuple = ("apple")         # 定义元组
print(tuple[0])           # 打印第一个元素
print (type(tuple))        # 打印定义的tuple的类型

tuple = ("apple",)        # 定义元组，注意后面的逗号不可少
print (tuple[0])          # 打印第一个元素
print (type(tuple))      # 打印定义的tuple的类型

tuple = ("apple", "banana", "grape", "orange")     # 定义元组
print (tuple[-1])
print (tuple[-2])
tuple2 = tuple[1:3]                       # 分片,第二个元素到第三个元素(不包括第四个)
tuple3 = tuple[0:-2]                    # 分片，从第一个元素到倒数第二个元素(不包括倒数第二个)
tuple4 = tuple[2:-2]                    # 分片，从第三个元素到倒第二个元素(不包括倒数第二个)
print (tuple2)
print (tuple3)
print (tuple4)

fruit1 = ("apple", "banana")
fruit2 = ("grape", "orange")
tuple = (fruit1, fruit2)
print (tuple)
print ("tuple[0][1] =", tuple[0][1])
print ("tuple[1][1] =", tuple[1][1])
print ("tuple[1][1] =", tuple[1][2])

#打包
tuple = ("apple", "banana", "grape", "orange")
#解包
a, b, c, d = tuple
print (a, b, c, d)

tuple = (("apple", "banana"),("grape", "orange"),("watermelon",),("grapefruit",))
for i in range(len(tuple)):
    print ("tuple[%d] :" % i, "" ,)
    for j in range(len(tuple[i])):
        print (tuple[i][j], "" ,)
    print()
