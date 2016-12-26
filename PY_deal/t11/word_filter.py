# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import string
class Word_Filter:
    def __init__(self):
        self.list = []
        self.word_filter=[]
        f = open('filter.txt')
        context = f.readlines()
        f.close()
        for word in context:
            self.list.append(word)
        self.list = map(string.strip, self.list)

    def Word_Check(self, sentence):
        Flag = False
        for sss in self.list:
            if sss in sentence:
                self.word_filter.append(sss)
                Flag = True
        return Flag

    def Get_Word_filter(self):
        return self.word_filter

if __name__ == '__main__':
    CHeck = Word_Filter()
    word_filter =[]
    a = raw_input()
    while 1:
        if CHeck.Word_Check(a):
            # print 'hace ...'
            word_filter = CHeck.Get_Word_filter()
            for word in word_filter:
                a = a.replace(word, '*' * len(word.decode('utf-8')))
        else:
            print 'none'

        print a
        a = raw_input()
        if a == 'Q' or a == 'q':
            break







