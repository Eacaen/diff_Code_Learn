# yield与return区别
def func(n):
    for i in range(n):
        return i
def func2(n):
    for i in range(n):
        yield i

print (func(3))
f = func2(3)
print (f)
print (f.next())
print (f.next())
