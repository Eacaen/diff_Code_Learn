# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os 
import re

def ensure_dir(f):
	d = os.path.dirname(f)
	if not os.path.exists(d):
		os.makedirs(d)

def ensure_file( f ):
	if not os.path.isfile( f ):
		txt = os.mknod( f )

class ZhihuimgPipeline(object):

	# def __init__(self):
	# 	pass
 	# 	self.dir = str("./") + self.file_name + str("/")
		# ensure_dir(self.dir)
		# self.img_url_list_txt = str ( self.dir + self.file_name +'.txt' )
		# ensure_file( self.img_url_list_txt )

		# self.img_url_list = self.get_img_url_list()
		# self.img_name = len(self.img_url_list) + 1

	def open_spider(self, spider):
		self.file_name = str (spider.ques_num )
 
 		self.dir = str("./") + self.file_name + str("/")
		ensure_dir(self.dir)
		self.img_url_list_txt = str ( self.dir + self.file_name +'.txt' )
		ensure_file( self.img_url_list_txt )

		self.img_url_list = self.get_img_url_list()
		self.img_name = len(self.img_url_list) + 1

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

	def process_item(self, item, spider):
		if_exist = 0

		img_urls = item['img_url']
		for i in range(len( img_urls )):
			if img_urls[i]   in self.img_url_list:
				print  if_exist ,  'exist'	
				if_exist = if_exist +1  

			if img_urls[i] not in self.img_url_list:
					# if saveImg:
					#	 la = str(img_urls[i].split('.')[-1])
					# 	self.saveImg(img_urls[i] , mdir = self.dir , filename = str(self.img_name) + '.'+ la)
					# 	print self.img_name, '    ', la

				url_write = str(self.img_name) + '. ' + str( img_urls[i] ) + '\n'
				self.Write_file(url_write, mdir= self.dir , filename = self.file_name +'.txt' , mode='a')
				self.img_name = self.img_name +1

		return item
