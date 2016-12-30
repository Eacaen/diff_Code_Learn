list = ["apple", "banana", "grape", "orange"]     # 定义列表
print (list)
print (list[2])
list.append("watermelon")                # 列表末尾添加元素
list.insert(1, "grapefruit")                 # 列表中插入元素
print (list)
list.remove("grape")                     # 列表中移除grape
print (list)
list.remove("a")                        # 列表中移除a，因为当前列表中并没有a，所以将抛错
print (list.pop())                        # 打印从列表中弹出的元素，即最后一个元素
print (list)

list = ["apple", "banana", "grape", "orange"]
print (list[-2])
print (list[1:3])
print (list[-3:-1])
list = [["apple", "banana"],["grape", "orange"],["watermelon"],["grapefruit"]]
for i in range(len(list)):             # 遍历列表
    print ("list[%d] :" % i, "" ,)
    for j in range(len(list[i])):
        print (list[i][j], "" ,)
    print()

list1 = ["apple", "banana"]
list2 = ["grape", "orange"]
list1.extend(list2)           # list1连接list2
print (list1)
list3 = ["watermelon"]
list1 = list1 + list3          # 将list1与list3连接后赋给list1
print (list1)
list1 += ["grapefruit"]       # 使用+=给list1连接上[“grapefruit”]
print (list1)
list1 = ["apple", "banana"] * 2
print (list1)

list = ["apple", "banana", "grape", "orange"]
print (list.index("grape"))        # 打印grape的索引
print (list.index("orange"))       # 打印orange的索引
print ("orange" in list)           # 判断orange是否在列表中

list = ["banana", "apple", "orange", "grape"]
list.sort()                              # 排序
print ("Sorted list:", list)
list.reverse()                          # 反转
print ("Reversed list:", list)

# 堆栈的实现
list = ["apple", "grape", "grape"]
list.append("orange")              # 将orange压入堆栈
print (list)
print ("弹出的元素：", list.pop())    # 从堆栈中弹出最后压入的元素
print (list)

#队列的实现
list = ["apple", "grape", "grape"]
list.append("orange")                  # 队尾加入orange
print (list)
print ("弹出的元素：", list.pop(0))       # 弹出第一个元素
print (list)
