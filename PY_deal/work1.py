# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
singer = ['The Rolling Stones','Beatles','Guns N Roses','Metalica']
song = ['Satisfaction','Let it Be','Dont Cry','Nothing Else matters']
comb = zip(singer,song)
qq = ['singer','song']
t = pd.DataFrame(comb,columns = qq)
print t
t.to_csv('soqng.csv')
t.to_excel('soqng.xlsx')
# print comb,type(comb)