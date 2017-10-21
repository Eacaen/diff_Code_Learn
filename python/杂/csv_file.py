# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import csv
villains = [
    ['doc','a'],
    ['rosr','b'],
    ['exic','c'],
]

with open('villains.csv','wt') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)

with open('villains.csv','rt') as fin:
    cin = csv.reader(fin)
    vas = [row for row in cin]

print vas