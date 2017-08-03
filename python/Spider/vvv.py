# -*- coding:utf-8 -*-
import re
import requests
import urllib2
import urllib
import cookielib
from bs4 import BeautifulSoup

follo_headers = {
	"Origin" : "https://www.zhihu.com",
	"Host":"www.zhihu.com",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Referer" : "https://www.zhihu.com/people/hehe-eacaen/following",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Connection" : "keep-alive"
}

logUrl = "https://www.zhihu.com/people/hehe-eacaen/following"
logUrl2  ="https://unpkg.zhimg.com/za-js-sdk@2.3.2/dist/zap.js"

# req = urllib2.Request(logUrl , headers=follo_headers )  
# data = urllib2.urlopen(req)
# cont = data.read()
# print cont

session = requests.Session()
r = requests.post(logUrl , headers=follo_headers , verify = False)
cont= r.text

soup =BeautifulSoup(cont, "lxml")
links = soup.find_all('a', class_ = "UserLink-link",\
	 href=re.compile(r'/people/(.*?)'),target="_blank")

number = soup.find_all("div", class_ ="NumberBoard-value")
print number

for link in links:
	print link['href']

