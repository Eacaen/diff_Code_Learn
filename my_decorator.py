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

class Student(object):
    def __init__(self,value=60):
        self._score = value

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(60)
print s.get_score()
s.set_score(60000)
print s.get_score()
print s._score
