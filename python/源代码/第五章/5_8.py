# 多个return语句
def func(x):
    if x > 0:
        return "x > 0"
    elif x == 0:
        return "x == 0"
    else:
        return "x < 0"

print (func(-2))

# 多个return语句的重构
def func(x):
    if x > 0:
        result = "x > 0"
    elif x == 0:
        result = "x == 0"
    else:
        result = "x < 0"
    return result    

print (func(-2))  
