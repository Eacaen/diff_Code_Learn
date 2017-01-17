# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import pylab as plt

fig = plt.figure(figsize=(5,10))

figure_title = "Normal title"
ax1  = plt.subplot(1,2,1)

plt.title(figure_title, fontsize = 20)
plt.plot([1,2,3],[1,4,9])

figure_title = "Raised title"
ax2  = plt.subplot(1,2,2)

plt.text(0.5, 1.08, figure_title,
         horizontalalignment='center',
         fontsize=20,
         transform = ax2.transAxes)
plt.plot([1,2,3],[1,4,9])

plt.show()