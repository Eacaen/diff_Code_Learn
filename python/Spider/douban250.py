# -*- coding:utf-8 -*-
"""
爬取豆瓣TOP250的电影内容
"""
import re
import requests
import urllib2
from bs4 import BeautifulSoup
import pandas as pd
import collections

import sys
reload(sys)
sys.setdefaultencoding('utf8')

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
    # name = [str(i) for i in name]
    return name


session = requests.Session()
start_page = 0
while start_page <= 225:
    Top250 = collections.OrderedDict()
    other_name_list = [ ]
    score_list = []
    director_list = [ ]

    logUrl = 'https://movie.douban.com/top250?start=' + str(start_page) + '&filter='

    r = session.get(logUrl )
    soup =BeautifulSoup(r.content, "lxml")

    name_patt = re.compile(r'<span.*?class="title">(.*?)</span>')
    name = re.findall(name_patt , r.content)

    other_name = soup.find_all('span', class_ = "other")
    score = soup.find_all('span', class_ = "rating_num")

    director = soup.find_all('p', class_ = "")

    name_list = combine_name_list(name)
    for s in director:
            dd =  s.get_text().strip().replace('  ', '').replace('\n', '').replace('...', '/')
            dd = unicode(dd)
            director_list.append(dd)

    for i in other_name:

        other_name_list.append( unicode (i.string ) )

    for i in score:
        score_list.append( unicode (i.string ) )


    Top250['名字'] = name_list 
    Top250['分数'] = score_list 
    Top250['别名'] = other_name_list 
    Top250['简介'] = director_list 

    df = pd.DataFrame(Top250 , index = range(start_page+1 , start_page+1 + 25))
    print df

    # writer = pd.ExcelWriter('Top250.xlsx', engine='openpyxl')
    # df.to_excel(writer )
    # df.to_excel(writer, startrow=len(df)+1 )
    # writer.save()
    if start_page == 0:
        df.to_excel('Top250.xlsx')

    if start_page > 0:
        df_bef = pd.read_excel('Top250.xlsx') 

        pd.concat([df_bef, df ]).to_excel('Top250.xlsx')
    
    start_page = start_page + 25 
 
 


 