# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
#属性设置
class Duck():
    def __init__(self,input_name):
        self.hidden_name = input_name
    def get_name(self):
        print 'inside the getter'
        return self.hidden_name
    def set_name(self,input_name):
        print 'inside the setter'
        self.hidden_name = input_name
    name = property(get_name,set_name)

fowl = Duck('Howard')
print fowl.name
print '\n'
fowl.set_name('Daffy')
print fowl.name