# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
#subplot实例
#修改坐标plt.xticks的字体大小
#来源网络

import matplotlib.pyplot as plt
import numpy as np
from numpy import abs

size=[5,10,20,30,50,100]
avg=[-0.2896,0.073865632,0.034858287,-0.092241705,-0.022924236,0.016541661]
avr=[0.032,0.077757872,0.090351641,0.036522663,0.034413038,0.096587464]

fig = plt.figure()

ax1 = fig.add_subplot(211)
lns1 = ax1.plot(size,color='blue',label='error average',linestyle='-',linewidth=1.9)
ax1.set_ylabel('deviation from\ncentral line ($m$)',fontsize=18, labelpad = 0.5)

plt.xticks(fontsize = 17)#对坐标的值数值，大小限制
plt.yticks(fontsize = 17)

ax2 = fig.add_subplot(212)
ax2.set_ylabel('standard \nvariance ($m^2$)',fontsize=18,labelpad = 12.5)
lns2 = ax2.plot(size, avr, color='red',label='mean square error',linestyle='-',linewidth=1.9)

plt.xticks(fontsize = 17)#对坐标的值数值，大小限制
plt.yticks(fontsize = 17)
ax2.set_xlabel('replay size',fontsize=18)

plt.subplots_adjust(left=0.18, wspace=0.25, hspace=0.25,
                    bottom=0.13, top=0.91)

#plt.text(0.4, 0.4, 'deviation from\n central line ($m$)', rotation=90, ha='left')

#plt.legend(prop={'size':18})  # loc='upper left',

#fig.savefig('./figure/error_paper.eps', format='eps', dpi=1000)
# fig.savefig('./figure/error_paper.png', dpi=1000)

plt.show()