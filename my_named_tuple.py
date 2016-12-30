# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
from collections import namedtuple
# Duck = namedtuple('Duck','bill tail')
# duck = Duck('wide orange','long')
# print duck

Ducks = namedtuple('Ducka','aaa sss ddd')
parts = {'aaa':'wide orange', 'sss':'long'}
parts['ddd'] = 'add ddd'
duck2 = Ducks(**parts)
print duck2.ddd