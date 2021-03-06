# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

def _list_mut(list1,list2):
    return list(map(lambda x: x[0] * x[1], zip(list1, list2)))

data = pd.read_excel("T06_10.xlsx",sheetname=0)

Q = data.iloc[10,:]
Q = [num*1e-4 for num in Q]

Epsilon = [1/x*math.log(0.9/0.6) for x in Q]

#####################################
Ft = [num*1.0/11 for num in range(1,11)]
Alpha_all = []
Beta_all =[]
Fig_name = [
    'fig_1',
    'fig_2',
    'fig_3',
    'fig_4',
    'fig_5',
    'fig_6',
    'fig_7',
    'fig_8',

]
for i in range(1,len(data.columns)+1):
    T = data[i][0:10]
    T = list(T)
    T.sort()
    Length = len(T)

    Yk = map(math.log , [num - Epsilon[i-1] for num in T] )
    Zk = [math.log( math.log(1/(1-x) ) ) for x in Ft]

    Alpha1 = Length*sum(_list_mut(Yk,Zk)) - sum(Yk) * sum(Zk)
    Alpha2 = Length*sum(_list_mut(Yk,Yk)) - sum(Yk) * sum(Yk)
    Alpha = Alpha1/Alpha2
    Alpha_all.append(Alpha)
    Beta_pre = (Alpha * sum(Yk) - sum(Zk)) / (Alpha*10)

    Beta = math.exp(Beta_pre)
    Beta_all.append(Beta)

    c = np.polyfit(Yk, Zk, 1)  # 拟合多项式的系数存储在数组c中
    yy = np.polyval(c, Yk)  # 根据多项式求函数值

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(Yk, Zk, 'o', Yk, yy)
    ax1.set_xlabel('Yk')

    ax1.set_ylabel('Zk ')
    # ax1.set_ylim(-2.5,1)
    # ax1.set_yticks(Zk)  # 设置刻度

    ax2 = ax1.twiny()  # this is the important function
    tt = [int(x/1000) for x in T]

    plt.xticks(fontsize=10)  # 设置坐标字体大小

    ax2.set_xlabel('T/' + r'$\ 10^3$')
    ax2.set_xticks(tt)
    ax2.set_xticklabels(tt)

    ax2 = ax1.twinx()
    ax2.set_ylabel('F(t)')
    ax2.set_ylim(-2.5, 1)
    ax2.set_yticks(Zk)  # 设置刻度
    ax2.set_yticklabels([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

    epsilon = '%.2f' %Epsilon[i-1]
    alpha = '%.2f' %Alpha
    beta = '%.2f' %Beta

    aaa = (Yk[9] - Yk[0]) * 0.5 + Yk[0]
    bbb = (Zk[9] - Zk[0]) * 0.25 + Zk[0]
    plt.text(aaa, bbb, r'$\epsilon=$' + epsilon + r'$,\ \alpha=$' + alpha + r'$,\ \beta=$' + beta)
    # fig.savefig(Fig_name[i-1])
    plt.show()

dir = {'Epsilon':Epsilon,'Alpha':Alpha_all,'Beta':Beta_all}
frame = pd.DataFrame(dir)
print frame
frame.to_excel('result.xlsx')


