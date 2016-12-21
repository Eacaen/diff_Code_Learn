def compareNum(num1, num2):
    if(num1 > num2):
        return str(num1)+" > "+str(num2)
    elif(num1 < num2):
        return str(num1)+" = "+str(num2)
    elif(num1 == num2):
        return str(num1)+" = "+str(num2)
    else:
        return ""

num1 = 2
num2 = 1
print (compareNum(num1, num2))
num1 = 2
num2 = 2
print (compareNum(num1, num2))
num1 = 1
num2 = 2
print (compareNum(num1, num2))
