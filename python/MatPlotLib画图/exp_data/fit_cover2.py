# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

import pandas as pd
import math
Y = [8.653671849,
    8.8526732319,
    8.9612547244,
    9.0021167222,
    9.3774489689,
    9.4171997384,
    9.6929107127,
    9.8101871357,
    9.937897002,
    10.083254853]
Z = [-2.3506186555,
    -1.6060900455,
    -1.1442780857,
    -0.7941060118,
    -0.5006512197,
    -0.2376769509,
    0.011534137,
    0.2618125616,
    0.5334173533,
    0.8745913829]

Ft = [num*1.0/11 for num in range(1,11)]
t = [28331.95037,
    29419.34823,
    15742.2359,
    11661.89312,
    17436.27694,
    16253.52914,
    11655.16305,
    12171.11502,
    32598.81557,
    33403.69742,
    ]
T = [num/100.0 for num in t]
T.sort()

c=np.polyfit(Y,Z,1)#拟合多项式的系数存储在数组c中
yy=np.polyval(c,Y)#根据多项式求函数值
# ax2.plot(Y,Z,'o',Y,yy)

fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.plot(Y,Z,'o',Y,yy)

yy = list(set([round(x,2) for x in Y]))
yy.sort()
plt.xticks(fontsize = 10)#设置坐标字体大小
ax1.set_xlabel('T/'+r'$\ 10^3$')
ax1.set_xticks(yy)
ax1.set_xticklabels([int(num)/10 for num in T])

ax1.set_ylabel('Ft')
ax1.set_ylim(-2.5,1)
ax1.set_yticks(Z) #设置刻度
ax1.set_yticklabels([0.1,  0.2,  0.3,  0.4,  0.5,  0.6,  0.7,  0.8,  0.9 , 1.0])

plt.text(0.05, 1.07,'FFFFFFFFFFFFFFF',
         fontsize=14,
         transform = ax1.transAxes)

ax2 = ax1.twinx()
ax2.set_ylabel('Z ')
ax2.set_ylim(-2.5,1)

ax2 = ax1.twiny()  # this is the important function
ax2.set_xlabel('Y',fontsize=10)
yyy = list(set([int(x) for x in Y]))
yyy.sort()

yyy = np.arange(yyy[0],yyy[-1]+1,(yyy[-1] +1 - yyy[0])/5.0)
print 'yyy',yyy
# ax2.set_xticks(yy) #设置刻度
plt.text(0.05, 1.07,'FFFFFFFFFFFFFFF',
         fontsize=14,
         transform = ax1.transAxes)
ax2.set_xticklabels(yyy)

plt.show()