# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
#正则表达式
import re
r = re.search('n.*','Young Naive can not do it any more')
print r.group()
r = re.findall('n','Young Naive can not do it any more')
print r
r = re.split('n','Young Naive can not do it any more')
print r
r = re.sub('n','##','Young Naive can not do it any more')
print r