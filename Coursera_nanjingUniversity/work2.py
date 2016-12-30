# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
t = pd.read_csv('eeeee.csv')
# t = pd.DataFrame(comb,columns = qq)
# print t
# t.to_csv('soqng.csv')
# t.to_excel('soqng.xlsx')

t['sum'] = t['Python'] + t['Math']
print t
t.to_csv('eeeee.csv',mode='a+')
