# -*- coding:utf-8 -*-
import urllib2
import re
import requests
import os
import json
import urllib

s = u'\u5168\u7403\u7ecf\u5178IT\u6570\u7801\u6392\u884c\u699c'.encode('utf-8')
# print s

reee =  'dwefwf wrefwerg vrwf \
<img src="https://pic2.zhimg.com/v2-1492679bb23923eda0eb29e5f73d4d1d_b.png" \
<img src="//zhstatic.zhihu.com/assets/zhihu/ztext/whitedot.jpg"\
<img src="https://pic2.zhimg.com/v2-1492679bb23923eda0eb29e5f73d4d1d_b.jpg"\
<img src="https://pic2.zhimg.com/v2-1492679bb23923eda0eb29e5f73d4d1d_b.jpg"\
<img src="https://pic2.zhimg.com/v2-1492679bb23923eda0eb29e5f73d4d1d_b.jpg" \
"\n'

# img_urls = re.findall('img src="(https:.*?)"', reee)
# print img_urls
# print img_urls[1].split('.')[-1]

def Write_file(content,filename=None):
	file =  filename
	f = open(file,'a')
	f.write(content)
	f.close()

# Write_file(reee,'zhuhu.txt')
def ensure_dir(f):
	d = os.path.dirname(f)
	if not os.path.exists(d):
		os.makedirs(d)

# ensure_dir('./img/')

follo_headers = {
	"Origin" : "https://www.zhihu.com",
	"Host":"www.zhihu.com",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
	"Referer" : "https://www.zhihu.com/question/30460976",
	 "Accept-Language":"zh-CN,zh;q=0.8",
	"Connection" : "keep-alive",
	"Accept-Encoding":"gzip, deflate, br",
	"authorization":"Bearer Mi4wQUlCQ0pOSHVJQXdBVUFJSlVSSWhEQmNBQUFCaEFsVk43MmVoV1FCbklIYzJIZmoyY2lELWRIdGZxZWlzZ3ZqSDRB|1501158127|bcb9ccfecd888845e2e5d75c110617c33062a836",
}

# dir = str("./")+str(follo_headers['Referer'].split('/')[-1])+str("/")
# print f
# ensure_dir(dir)

# offset = 0
# while offset < 5:
# 	print offset
# 	offset = offset + 20
# 	print offset

# mm = './49364343/'
# d = os.listdir(mm)
# print d,len(d)
# 49364343.txt

with open('./49364343/49364343.txt' , 'r ') as f:
	red = f.read()

print red , type(red)
# print red.split(' ')

patton = re.compile('(https://.*?)\n')
img_url_list = re.findall(patton , red)
print img_url_list, type(img_url_list) , len(img_url_list)
for i in img_url_list:
	print i

d = os.path.isfile('test.txt')
print d
