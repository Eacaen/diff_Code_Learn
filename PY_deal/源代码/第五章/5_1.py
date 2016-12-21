def func(x): 
    if x > 0:
        return x

print (filter(func, range(-9, 10)))        # 调用filter函数,返回的是filter对象
print(list(filter(func, range(-9, 10)))     # 将filter对象转换为列表
