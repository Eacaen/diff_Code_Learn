# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import pandas as pd
import string

f = open('word.txt','r')
a = f.read()
delset = string.punctuation.translate(None,'-\\\'')
#!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# print delset
a = a.translate(None,delset).lower().split()
# a = a.lower()
# a = a.split()
# print a,type(a)

list_word = []
list_num = []
for s in a:
    if s in list_word:
        d = list_word.index(s)
        # print d
        list_num[d] += 1
    else:
        # print s
        list_word.append(s)
        k = len(list_word)
        # print k
        list_num.append(1)
        # print list_word

# print list_word,list_num
dict = zip(list_word,list_num)
# print dict
qq = ['word','num']
exca = pd.DataFrame(dict,columns = qq)
exca = exca.sort(columns='num',ascending=False)
exca = exca.reset_index(drop=True)
exca.to_csv('word_statistics.csv')
# exca.to_excel('word_statistics.xlsx')
print exca




