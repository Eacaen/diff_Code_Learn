# 带else子句的while循环
x = float(input("输入x的值："))        # 接收用户输入的数字并转换为float类型
i = 0
while(x  != 0):                     # python3中不等于抛弃了<>，一律使用!=
    if(x > 0):
        x -= 1                      # 如果x大于0则减1
    else:
        x += 1                     # 如果x小于0则加1
    i = i + 1
    print( "第%d次循环：" %(i, x))
else:
    print ("x等于0：", x)
