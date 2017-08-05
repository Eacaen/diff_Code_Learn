# -*- coding:utf-8 -*-
import re
import requests
import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import collections

Top250 = collections.OrderedDict()
other_name_list = [ ]
score_list = []
director_list = [ ]

def combine_name_list(name_list):
    name = []
    i = 0
    while 1:
        if name_list[i+1].find("&nbsp") == 0:
            name.append(name_list[i] + name_list[i+1].replace("&nbsp",''))
            i = i + 2
        if i >= len(name_list) :
            break
        if name_list[i+1].find("&nbsp") == -1: 
            name.append(name_list[i])
            i = i + 1
        if i >= len(name_list) :
            break
    name = [i.replace(';', ' ')  for i in name]
    return name


session = requests.Session()
logUrl = 'https://movie.douban.com/top250?start=0&filter='

r = session.get(logUrl )

soup =BeautifulSoup(r.content, "lxml")

name_patt = re.compile(r'<span class="title">(.*?)</span>')
name = re.findall(name_patt , r.content)

for i in name:
    print i
# other_name = soup.find_all('span', class_ = "other")
# score = soup.find_all('span', class_ = "rating_num")

# director = soup.find_all('p', class_ = "")

# name_list = combine_name_list(name)
# for s in director:
#         dd =  s.get_text().strip().replace('  ', '').replace('\n', '').replace('...', '/')
#         dd = unicode(dd)
#         director_list.append(dd)



