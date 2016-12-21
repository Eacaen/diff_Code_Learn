dict = {"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}
print (dict)
print (dict["a"])         # 打印键a对应的值

dict = {1 : "apple", 2 : "banana", 3 : "grape", 4 : "orange"}
print (dict)
print (dict[2])

#字典的添加、删除、修改操作
dict = {"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}
dict["w"] = "watermelon"
del(dict["a"])                    # 删除字典中键为a 的元素
dict["g"] = "grapefruit"            # 修改字典中键为g的值
print (dict.pop("b"))              # 弹出字典中键为b的元素
print (dict)
dict.clear()                     # 清除字典中所有元素
print (dict)

#字典的遍历
dict = {"a" : "apple", "b" : "banana", "g" : "grape", "o" : "orange"}
for k in dict:
    print ("dict[%s] =" % k,dict[k])

#字典items()的使用
dict = {"a" : "apple", "b" : "banana", "c" : "grape", "d" : "orange"} 
print (dict.items())

#使用列表、字典作为字典的值
dict = {"a" : ("apple",), "bo" : {"b" : "banana", "o" : "orange"}, "g" : ["grape","grapefruit"]}
print (dict["a"])
print (dict["a"][0])
print (dict["bo"])
print (dict["bo"]["o"])
print (dict["g"])
print (dict["g"][1])

dict = {"a" : "apple", "b" : "banana", "c" : "grape", "d" : "orange"} 
#输出key的列表
print (dict.keys())
#输出value的列表
print (dict.values())

#get()的等价语句
D = {"key1" : "value1", "key2" : "value2"}
if "key1" in D:
    print (D["key1"])
else:
    print ("None")

#字典中元素的获取方法
dict = {"a" : "apple", "b" : "banana", "c" : "grape", "d" : "orange"} 
print (dict)
print (dict.get("c", "apple"))          # 使用get获取键为c的值，若不存在返回默认值apple
print (dict.get("e", "apple"))          # 使用get获取键为e的值，若不存在返回默认值apple

#udpate()的等价语句
D = {"key1" : "value1", "key2" : "value2"}
E = {"key3" : "value3", "key4" : "value4"}
for k in E:
    D[k] = E[k]
print (D)

#字典E中含有字典D中的key
D = {"key1" : "value1", "key2" : "value2"}
E = {"key2" : "value3", "key4" : "value4"}
for k in E:
    D[k] = E[k]
print (D)

#字典的更新
dict = {"a" : "apple", "b" : "banana"}
print (dict)
dict2 = {"c" : "grape", "d" : "orange"}
dict.update(dict2)                # 使用update方法更新dict
print (dict)

# 设置默认值
dict = {}
dict.setdefault("a")
print (dict)
dict["a"] = "apple"
dict.setdefault("a", "None")
print (dict)

#调用sorted()排序
dict = {"a" : "apple", "b" : "grape", "c" : "orange", "d" : "banana"} 
print (dict)   
#按照key排序  
print (sorted(dict.items(), key=lambda d: d[0]))
#按照value排序  
print (sorted(dict.items(), key=lambda d: d[1]))

#字典的浅拷贝
dict = {"a" : "apple", "b" : "grape"} 
dict2 = {"c" : "orange", "d" : "banana"} 
dict2 = dict.copy()           # 拷贝dict并赋给dict2
print (dict2)

#字典的深拷贝
import copy
dict = {"a" : "apple", "b" : {"g" : "grape","o" : "orange"}} 
dict2 = copy.deepcopy(dict)         # 深拷贝
dict3 = copy.copy(dict)              # 浅拷贝
dict2["b"]["g"] = "orange"
print (dict)
dict3["b"]["g"] = "orange"
print (dict)
