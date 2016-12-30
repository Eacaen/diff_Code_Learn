# 函数的默认参数
def arithmetic(x=1, y=1, operator="+"):
    result = {
        "+" : x + y,
        "-" : x - y,
        "*" : x * y,
        "/" : x / y 
    }
    return result.get(operator)     # 返回计算结果

print (arithmetic(1, 2))
print (arithmetic(1, 2, "-"))
print (arithmetic(y=3, operator="-"))
print (arithmetic(x=4, operator="-"))
print (arithmetic(y=3, x=4, operator="-"))
