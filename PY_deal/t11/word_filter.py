# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import string
class Word_Filter:
    def __init__(self):
        self.list = []
        f = open('filter.txt')
        context = f.readlines()
        f.close()
        for word in context:
            self.list.append(word)
        self.list = map(string.strip, self.list)
        # print self.list

    def Word_Check(self, word):
        for sss in self.list:
            # print sss
            if word == sss:
                return True
        return False

if __name__ == '__main__':
    CHeck = Word_Filter()
    a = raw_input()
    while 1:
        # print a, type(a)
        if CHeck.Word_Check(a):
            print 'hace ...'
        else:
            print 'none'
        a = raw_input()
        if a == 'Q' or a == 'q':
            break







