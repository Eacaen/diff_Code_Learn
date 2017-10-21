# -*- coding: utf-8 -*-
# __author__ = 'eacaen'


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import argparse

##命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('file')     #输入文件
parser.add_argument('-o', '--output')   #输出文件


##获取参数
args = parser.parse_args()
PATH = args.file
OUTPUT = args.output

t = pd.read_excel(PATH,encoding='gb2312',sheetname=0)

# t = pd.read_excel("exp1.xlsx",sheetname=0)
print type(t)
print t.columns
# print t[u'时间']
time = t[u'时间'] - t.iloc[1,0]
voltage = t[u'电压'] - t.iloc[2,0]

print time,voltage

plt.plot(time,voltage)
plt.xlabel('time')
plt.ylabel('voltage')
plt.title('time & voltage')
plt.grid(True)
# plt.legend()
# 字符画输出到文件
if OUTPUT:
    # plt.savefig("test.png")OUTPUT
    plt.savefig(OUTPUT)

plt.show()
