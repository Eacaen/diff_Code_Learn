# -*- coding:utf-8 -*-
import urllib2
import re
import requests
import os
import json
 
def ensure_dir(f):
	d = os.path.dirname(f)
	if not os.path.exists(d):
		os.makedirs(d)

def ensure_file( f ):
	if not os.path.isfile( f ):
		txt = os.mknod( f )

class zhihu_Img_spider(object):
	"""docstring for zhihu_Img_spider"""
	def __init__(self, question_num , url = None , offset = 0 , start_offset = 0 ,  img_patton = None):
		super(zhihu_Img_spider, self).__init__()
		self.question_num = question_num
		if url == None:
			self.url = 'https://www.zhihu.com/api/v4/questions/'+ str(self.question_num) + '/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&limit=20&offset='
		else:
			self.url = url 
		self.following = [ ]

		self.headers = {
		"Origin" : "https://www.zhihu.com",
		"Host":"www.zhihu.com",
		"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0",
		"Referer" : "https://www.zhihu.com/question/" + str( self.question_num) ,
		 "Accept-Language":"zh-CN,zh;q=0.8",
		"Connection" : "keep-alive",
		"Accept-Encoding":"gzip, deflate, br",
		"authorization":"oauth c3cef7c66a1843f8b3a9e6a1e3160e20",
				}

		self.file_name = str(self.headers['Referer'].split('/')[-1])
		self.dir = str("./")+self.file_name+str("/")
		ensure_dir(self.dir)

		self.img_url_list_txt = str ( self.dir + self.file_name +'.txt' )
		ensure_file( self.img_url_list_txt )

		self.img_url_list = self.get_img_url_list()
	
		self.offset = offset
		self.start_offset  = start_offset 
		self.img_name = len(self.img_url_list) + 1 #len(os.listdir(self.dir))

		self.img_patton = img_patton
	def get_content(self , url):
		proxy = {"http": "http://144.52.191.37:53281", "https": "49.87.49.137:8118"}
		r = requests.get( url  , headers = self.headers )#, proxies = proxy  )
		cont= r.text 
		txt=json.loads(cont)
		return txt

	def get_following(self , content):
		for pop in content["data"]:
			x = pop["content"]
			self.following.append( x )

	def saveImg( self , imageURL, mdir = None ,filename=None):
		im = urllib2.urlopen(imageURL , timeout = 5)
		ima = im.read()
		file =  str(mdir) + filename
		f = open(file,'w')
		f.write(ima)
		f.close()

	def Write_file(self , content , mdir = None , filename=None , mode = 'w'):
		file =  str(mdir) + filename
		f = open(file , mode)
		f.write(content)
		f.close()

	def get_img_url_list(self):
		with open(self.img_url_list_txt , 'r ') as f:
			red = f.read()
		patton = re.compile('(https://.*?)\n')
		img_url_list = re.findall(patton , red)
		return img_url_list

 
 	def get_following_list(self):
		while self.start_offset  <= self.offset:
			print self.start_offset
			get_url = self.url + str( self.start_offset ) + "&sort_by=default"
			Con = self.get_content(get_url)
			self.get_following(Con)

 			if Con["paging"]['is_end' ]:
 				print self.start_offset
 				print '-----------------------------------------end of question -------------------------------------------'
				break

			self.start_offset = self.start_offset + 20

	def downloadImg_or_writeFile(self , saveImg = False):
		if_exist = 0
		for i in range(len(self.following)):
			img_patton = self.img_patton

			img_urls_truple = re.findall( img_patton , self.following[i].encode("utf-8")) 
			img_urls = set()
			for i in img_urls_truple:
				for j in i:
					img_urls.add(j)
			img_urls = list(img_urls)

			for i in range(len( img_urls )):
				if img_urls[i]   in self.img_url_list:
					print  if_exist ,  'exist'	
					if_exist = if_exist +1  

				if img_urls[i] not in self.img_url_list:
					la = str(img_urls[i].split('.')[-1])
					if saveImg:
						self.saveImg(img_urls[i] , mdir = self.dir , filename = str(self.img_name) + '.'+ la)
						
					print self.img_name, '    ', la
					url_write = str(self.img_name) + '. ' + str( img_urls[i] ) + '\n'
					self.Write_file(url_write, mdir= self.dir , filename = self.file_name +'.txt' , mode='a')
					self.img_name = self.img_name +1

		# url_write = '\n\n------------------------*------------------------*------------------------\n\n'
		# self.Write_file(url_write, mdir= self.dir , filename = self.file_name +'.txt' , mode='a')			

if __name__ == '__main__':
	# url = 'https://www.zhihu.com/api/v4/questions/20902967/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%28type%3Dbest_answerer\
	# %29%5D.topics&limit=20&offset='

	ques_code = 43551423 
	zhu_sp = zhihu_Img_spider( question_num = ques_code , offset = 10000 , start_offset = 0)

	# zhu_sp.img_patton = re.compile( 'img src="(https:.*?)"' )
	zhu_sp.img_patton = re.compile(r'img.*?src="(https:.*?)".*?data-original="(https:.*?)".*?data-actualsrc="(https:.*?)"')
	
	# zhu_sp.img_patton = r'img.*?src="(https:.*?)".*?data-original="(https:.*?)".*?data-actualsrc="(https:.*?)"'

	# zhu_sp.img_patton = r'data-original="([^"]+)"'
	# zhu_sp.img_patton = re.compile(r'img.*?src="(https:.*?)".*?data-original="(https:.*?)".*?"(https:.*?)"')

	zhu_sp.get_following_list( )
	zhu_sp.downloadImg_or_writeFile(saveImg=0)
	# for i in zhu_sp.img_url_list:
	# 	print i