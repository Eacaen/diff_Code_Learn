import urllib2
import re

class taobao_MM_spider(object):
	"""docstring for taobao_MM_spider"""
	def __init__(self):
 		self.siteURL = 'https://mm.taobao.com/json/request_top_list.htm'

	def getPage(self,pageIndex):
		url = self.siteURL+'?page='+str(pageIndex)
		requset = urllib2.Request(url)
		response = urllib2.urlopen(requset)
		return response.read().decode('gbk')

	def saveImg(self , imageURL,filename=None):
		im = urllib2.urlopen('http:'+imageURL)
		ima = im.read()
		file = './img/'+filename
		f = open(file,'w')
		f.write(ima)
		f.close()

	def getContents(self, pageIndex):
		cont = self.getPage(pageIndex)
		patternImg = re.compile('<img src="(.*?)"')
		patternName = re.compile('target="_blank">(.*?)</a>')
		images = re.findall(patternImg , cont)
		names = re.findall(patternName , cont)
		for i in range(len(images)):
			self.saveImg(images[i], names[i]+'.jpg')

if __name__=='__main__':
	MMT = taobao_MM_spider()
	for i in range(1,20):
		MMT.getContents(i)