def sum(x, y):
    return x + y
form functools import reduce                   # 引入reduce
print (reduce(sum, range(0, 10)))
print (reduce(sum, range(0, 10), 10))
print (reduce(sum, range(0, 0), 10))
