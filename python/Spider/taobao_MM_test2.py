import urllib2
import re
url = 'https://mm.taobao.com/json/request_top_list.htm?page=3'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
cc = response.read().decode('gbk')
patternImg = re.compile('<img src="(.*?)"')
patternName = re.compile('target="_blank">(.*?)</a>')
images = re.findall(patternImg , cc)
names = re.findall(patternName , cc)
for f in images:
	print 'http:'+f
for f in names:
	print f
# print images,names
def saveImg(imageURL,filename=None):
	im = urllib2.urlopen('http:'+imageURL)
	ima = im.read()
	file = './img/'+filename
	f = open(file,'w')
	f.write(ima)
	f.close()
	
for i in range(len(images)):
	saveImg(images[i], names[i]+'.jpg')
 