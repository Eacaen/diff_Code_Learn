# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
fin = open('bfile.txt','r')
# s = fin.readlines()
# print s
print fin.seek(2,0)
print fin.tell()