# import pandas as pd
#
# dats = {"name":['a','c'],'pay':[111,222]}
# frame = pd.DataFrame(dats)
# print frame
# frame.name = 'thrust'
# print frame
from pandas import Series, DataFrame
data = {'language': ['Java', 'PHP', 'Python', 'R', 'C#'],
            'year': [ 1995 ,  1995 , 1991   ,1993, 2000]}
frame = DataFrame(data)
frame['IDE'] = Series(['Intellij', 'Notepad', 'IPython', 'R studio', 'VS'])
print frame
print frame.IDE.values
print 'VS' in frame['IDE'].values

aaa = {'a':[1,2,3],'b':[4,5,6]}
print aaa
print 'a' in aaa