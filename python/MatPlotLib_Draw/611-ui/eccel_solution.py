# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
#修改了T06中的BUG
#互换了双轴坐标,实现完整绘图
#调整了坐标轴字体大小
#增加图例换行
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import math
import platform

sysstr = platform.system()
if(sysstr =="Windows"):
    zhfont_song = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
elif(sysstr == "Linux"):
    zhfont_song = matplotlib.font_manager.FontProperties('/usr/share/fonts/Windows/Fonts/simsun.ttc')


def _list_mut(list1,list2):
    return list(map(lambda x: x[0] * x[1], zip(list1, list2)))

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
title_name = [
    u'YK2563 - 1系列TTCI',
    u'YK2563 - 2系列TTCI',
    u'DK2564 - 1系列TTCI',
    u'DK2564 - 2系列TTCI',
    u'JT2566 - 1系列TTCI',
    u'JT2566 - 2系列TTCI',
    u'WB2567 - 1系列TTCI',
    u'WB2567 - 2系列TTCI'
]
def Soluton(name_in = '/home/eacaen/PY_deal/GUI/611-paji/T06_10.xlsx'
            ,name_out = 'result'):
    name_in = str(name_in)
    name_out = str(name_out)
    data = pd.read_excel(name_in,sheetname=0)

    Q = data.iloc[10,:]
    Q = [num*1e-4 for num in Q]

    Epsilon = [1/x*math.log(0.9/0.6) for x in Q]

#####################################
    Ft = [num*1.0/11 for num in range(1,11)]
    Alpha_all = []
    Beta_all =[]

    for i in range(1,len(data.columns)+1):
    # for i in range(1, 2):
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


        epsilon = '%.2f' % Epsilon[i - 1]
        alpha = '%.2f' % Alpha
        beta = '%.2f' % Beta

        aaa = (Yk[9] - Yk[0]) * 0.5 + Yk[0]
        bbb = (Zk[9] - Zk[0]) * 0.25 + Zk[0]
        plt.text(aaa, bbb, r'$\epsilon=$' + epsilon +'\n'
                            r'$\alpha=$' + alpha +'\n'
                            r'$\beta=$' + beta)


        aix_T = np.arange(T[0],T[9],(T[9] - T[0])/9)
        aix_Yk = map(math.log, [num - Epsilon[i - 1] for num in aix_T])

        plt.xticks(fontsize=8)  # 设置坐标字体大小
        ax1.set_xlabel('T/' + r'$\ 10^3$')
        ax1.set_xticks(aix_Yk)
        # ax1.set_xticklabels(([round(x / 1000.0, 1) for x in aix_T]))
        ax1.set_xticklabels(([int(x / 1000.0) for x in aix_T]))

        ax1.set_ylabel('F(t)')
        ax1.set_ylim(-2.5, 1)
        ax1.set_yticks(Zk)  # 设置刻度
        ax1.set_yticklabels([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])


        # plt.text(0.05, 1.07, title_name[i-1],
        #      fontsize=14,
        #      transform=ax1.transAxes,
        #     fontproperties=zhfont_song)


        ax2 = ax1.twinx()
        ax2.set_ylabel('Zk ')
        ax2.set_ylim(-2.5, 1)

        ax2 = ax1.twiny()  # this is the important function
        ax2.set_xlabel('Yk ',fontsize=10)
        yyy = list(set([int(x) for x in Yk]))
        yyy.sort()

        yyy = np.arange(yyy[0], yyy[-1] + 1, (yyy[-1] +1 - yyy[0])/5.0)
        ax2.set_xticklabels(yyy)

        # fig.savefig(Fig_name[i-1])

        # plt.show()

    dir = {'Epsilon':Epsilon,'Alpha':Alpha_all,'Beta':Beta_all}
    frame = pd.DataFrame(dir)
    frame.to_excel(name_out+'.xlsx')
    return frame


