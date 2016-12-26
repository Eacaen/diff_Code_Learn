
# coding:utf-8
from matplotlib.finance import _quotes_historical_yahoo
from datetime import date
from datetime import datetime
import pandas as pd

today = date.today()
start = (today.year - 1,today.month , today.day)
list1 = []
field = ['date','open','close','high','low','volume']
quotes = _quotes_historical_yahoo('AXP',start,today)
for i in range(0,len(quotes)):
    x = date.fromordinal(int(quotes[i][0]))  #转换成常规时间
    y = datetime.strftime(x,'%Y-%m-%d')      #转成固定格式
    list1.append(y)

quotessdf = pd.DataFrame(quotes,index=list1,columns=field)
# print quotessdf
# quotessdf.to_csv('ttt.csv')
# quotessdf.to_excel('ttt.xlsx')
# print quotessdf.index
# print quotessdf.columns
# print quotessdf.describe
# print quotessdf.iloc[1:2,]
print quotessdf[quotessdf.close>74]

