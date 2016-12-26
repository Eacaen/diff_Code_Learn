# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import string,re
printable = string.printable
print printable
r = re.findall('\d',printable)
print r
r = re.findall('\s',printable)
print r
print '\u0115'