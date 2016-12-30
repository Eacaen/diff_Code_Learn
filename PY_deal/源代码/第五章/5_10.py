# 嵌套函数
def func():
    x = 1
    y = 2
    m= 3
    n = 4
    def sum(a, b):              # 内部函数
        return a + b
    def sub(a, b):              # 内部函数
        return a - b
    return sum(x, y) * sub(m, n)

print (func())
