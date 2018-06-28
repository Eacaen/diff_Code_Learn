#!/usr/bin/python  
#coding: utf-8  
  
import numpy as np  
import matplotlib.pyplot as plt  
  
x = np.linspace(0, 5 * np.pi, 1000)  
  
y1 = np.sin(x)  
y2 = np.sin(2 * x)  
  
plt.plot(x, y1, c = "g")  
plt.plot(x, y2, c = 'r')  
  
# fill_between 填充两个函数之间的区域  
# 两个函数之间的区域用黄色填充  
plt.fill_between(x, y1, y2, alpha = 0.5, facecolor = "yellow")  
  
plt.show() 