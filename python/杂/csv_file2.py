# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import csv
# with open('villains.csv','rt') as fin:
#     cin = csv.DictReader(fin,fieldnames=['first','last']) #指定列的名字
#
#     vas = [row for row in cin]
#
# print vas

vall = [
    {'last': 'a', 'first': 'doc'},
    {'last': 'asdd', 'first': 'sss'},
    {'last': 'b', 'first': 'rosr'},
    {'last': 'qqqq', 'first': 'zcsadcs'},
    {'last': 'c', 'first': 'exic'}
]
with open('vall.csv','wt') as fout:
    cout = csv.DictWriter(fout,['first','last'])
    cout.writeheader()
    cout.writerows(vall)