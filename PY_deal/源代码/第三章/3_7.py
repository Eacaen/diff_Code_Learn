operator = "+"
x = 1
y = 2
for case in switch(operator):        # switch只能用于for in循环中
    if case('+'):
        print (x + y)
        break
    if case('-'):
        print (x - y)
        break
    if case('*'):
        print (x * y)
        break
    if case('/'):
        print (x / y)
        break
    if case():                      # 默认分支
        print ("")
