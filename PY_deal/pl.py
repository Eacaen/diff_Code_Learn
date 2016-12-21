f = open('123.txt')
context = f.readlines()
print context[0],type(context[0])
ss = context[0].split()
print ss
print list(ss)

f.close()