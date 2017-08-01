# encoding=utf8  
import urllib2
import re
from bs4 import BeautifulSoup

class Tie_Ba_Spider(object):
	"""docstring for Tie_Ba_Spider"""
	def __init__(self, baseUrl , seeLZ):
		super(Tie_Ba_Spider, self).__init__()
		self.baseUrl = baseUrl 
		self.seeLZ = '?see_lz=' + str(seeLZ)

	def saveCont(self , mytxt ,filename=None):
		file = './tieba/'+filename
		f = open(file,'a')
		for coni in mytxt:
			f.write(coni.encode('utf-8'))
		f.close()

	def getPage_Content(self , pageNum):
		try:
			url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
			print url
			requset = urllib2.Request(url)
			response = urllib2.urlopen(requset)
			return response.read()

		except urllib2.URLError , e:
			if hasattr(e, 'reason'):
				print 'error' , e.reason
				return None

	def parse(self , html_cont):
		contents = [ ]
		next_line = u'\n-------------------------------------------------------------------------------------------------------------------------------------------\n'
		soup =BeautifulSoup(cc,'html.parser' )
		title_node = soup.find("h3", class_="core_title_txt pull-left text-overflow ")
		contents.append(title_node.get_text())
		contents.append(next_line) 
 		con = soup.find_all("div", class_="d_post_content j_d_post_content ")
		for i in con:
 			contents.append(i.get_text()) 
 			contents.append(next_line) 
 		return contents

	def get_Maxpage(self , html_cont):
		patternPage = re.compile(r'<span class="red">(.*?)</span>')
		result = re.search(patternPage,cc)
		return int( result.group(1)  )

	
if __name__=='__main__':
	baseURL = 'http://tieba.baidu.com/p/3138733512'
	tbs = Tie_Ba_Spider(baseURL , 1)
	cc =  tbs.getPage_Content(1)
	print tbs.get_Maxpage(cc)
	for i in range(1 , tbs.get_Maxpage(cc)+1 ):
		tbs = Tie_Ba_Spider(baseURL , 1)
		cc =  tbs.getPage_Content( i )	
		ttt =  tbs.parse(cc)
		tbs.saveCont(ttt , 'r.txt')
	# soup =BeautifulSoup(cc,'html.parser' )
	# title_node = soup.find("h3", class_="core_title_txt pull-left text-overflow ")
	# print title_node.get_text() , type(title_node.get_text())

	# file = open('./tieba/r.txt' , 'w')
 # 	con = soup.find_all("div", class_="d_post_content j_d_post_content ")
 # 	for i in con:
 # 		print '----------------------------------------------------------------------\n'
 # 		print i.get_text()
	# 	file.write(  i.get_text().encode('utf-8') )
	# 	file.write('\n--------------------------------------------------------------------------------------\n')
 # 	patternPage = re.compile(r'<span class="red">(.*?)</span>')
	# all_page = soup.find_all(patternPage)
	# print all_page

	# # pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
 #    	result = re.search(patternPage,cc)
 #    	print result.group() 
 #    	print result.group(1) 





		  


