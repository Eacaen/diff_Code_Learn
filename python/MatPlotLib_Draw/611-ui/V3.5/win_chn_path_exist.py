# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import os
import pandas as pd

path_in = 'D:/diff_Code_Learn/python/MatPlotLib画图/611-ui/V3.5/T06_101.xlsx'
bbb = path_in.decode('utf8').encode('gbk')

sss  = unicode(path_in, 'utf8').encode('gbk')

file_name=os.path.normcase(sss)

a = os.path.exists(sss)

data = pd.read_excel(sss, sheetname=0)

print a,data
