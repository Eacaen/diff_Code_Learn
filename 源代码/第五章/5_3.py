def power(x): return x ** x           
print (map(power, range(1, 5)))                                  # 打印map对象
print(list(map(power,range(1,5))))                                  # 转换为列表输出
def power2(x, y): return x ** y   
print (map(power2, range(1, 5), range(5, 1, -1)))                     # 打印map对象
print(list(map(power2, range(1, 5), range(5, 1, -1))))                  # 转换为列表输出