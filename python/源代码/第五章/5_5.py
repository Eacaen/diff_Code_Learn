# 传递可变参数
def search(*t, **d):
    keys = d.keys()
    values = d.values()
    print(keys)
    print (values)
    for arg in t: 
        for key in keys: 
            if arg == key:
                print ("find:",d[key])

search("one", "three", one="1",two="2",three="3")
