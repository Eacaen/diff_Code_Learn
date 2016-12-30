# -*- coding: utf-8 -*-
# __author__ = 'eacaen'

def search(*t,**d):
    keys = d.keys()
    values = d.values()
    print keys
    print values
    for arg in t:
        for key in keys:
            if arg == key:
                print "find =",d[key],type(d[key])
list = ["one" , "three"]
dirc = {"one" : "1" , "two" : "2" , "three" : "3"}
all = (list,dict)
print all
#search("one", "three",  one="1", two="2", three="3")
search("one", "three",  one= 1 , two= 2 , three = "the aaaa" )

