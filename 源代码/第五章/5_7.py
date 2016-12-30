# return返回多个值
def func(x, y, z):
    l = [x, y, z]
    l.reverse()
    numbers = tuple(l)
    return numbers

x, y, z = func(0, 1, 2)
print (x, y, z)
