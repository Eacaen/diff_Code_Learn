# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import scipy as sp
import pylab as pl
lista = sp.ones(50)
lista[10:30] = -10
# print lista,type(lista)
f = sp.fft(lista)
# print f
pl.plot(lista)
pl.plot(f)
pl.show()