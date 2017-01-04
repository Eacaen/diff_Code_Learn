# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import string
# s = 'hello world, 0001111'
# table = string.maketrans('','')#没有映射，保留原字符串
# s = s.translate(table) #hello world, 0001111
# print s

delset = string.punctuation
delset = delset.translate(None,'-\\\'')
#!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print delset,type(delset)

