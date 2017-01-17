# -*- coding: utf-8 -*-
# __author__ = 'eacaen'
import re
s = '''I wish i may, I wish I moght aswfish
        Have a dish of fish tonight.'''
# r = re.findall('wish|fish',s)
# print r
# r = re.findall('.',s)
# print r
# r = re.findall('^I wish',s)
# print r
# r = re.findall('fish$',s)
# print r
# r = re.findall('fish tonight$',s)
# print r
# r = re.findall('fish tonight\.$',s)
# print r
# r = re.split('[w|f]ish',s)
# print r
# r = re.findall('[wfh]t+',s)
# print r
# r = re.findall('ght\W',s)
# print r
# r = re.findall('I (?=wish)',s)
# print r
# r = re.findall('(?<=I )wish',s)
# print r
# r = re.findall(r'\b[w|f]ish',s)
# print r
# r = re.findall('[w|f]ish',s)
# print r
# r = re.findall('(?=ish)',s)
# print r

# m = re.search(r'(.dish\b).*(\bfish)',s)
# print m.group()
# print m.groups()
# m = re.search(r'(..dish\b.*\bfish)',s)
# print m.group()
# print m.groups()
#
m = re.search(r'(?P<Dish>..dish\b).*(?P<Fish>\bfish)',s)
# print m.groups()
# print m.group('Dish')
print(m.group())