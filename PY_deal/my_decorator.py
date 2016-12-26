# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
class Duck():
    def __init__(self,input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print 'inside the getter'
        return self.hidden_name

    @name.setter
    def name(self,input_name):
        print 'inside the setter'
        self.hidden_name = input_name

fowl = Duck('Howard')
print fowl.name
print '\n'
fowl.name = 'Daffy'
print fowl.name

