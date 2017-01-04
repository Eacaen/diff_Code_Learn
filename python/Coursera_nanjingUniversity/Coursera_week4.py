# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import numpy as np
from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import pandas as pd

today = date.today()
start = (today.year-2, today.month, today.day)
quotesMS = quotes_historical_yahoo('MSFT', start, today)
attributes=['date','open','close','high','low','volume']
quotesdfMS = pd.DataFrame(quotesMS, columns= attributes)
list = []
for i in range(0,len(quotesMS)):
    x = date.fromordinal(int(quotesMS[i][0]))
    y = date.strftime(x,'%y-%m-%d')
    list.append(y)
quotesdfMS.index = list
quotesdfMS = quotesdfMS.drop('date',axis=1)
quotesdfMS.to_excel("MSFT.xlsx")

list = []
for i in range(0,len(quotesdfMS)):
    list.append(int(quotesdfMS.index[i][3:5]))
quotesdfMS['month'] = list
# print quotesdfMS
quotesdfMS.to_excel("MSFT.xlsx")
a = (quotesdfMS.groupby('month').mean().close)
print type(a)
f = open('coursera_week4.txt','w')
f.write(a)
