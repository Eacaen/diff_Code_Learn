# -*- coding:utf-8 -*-
import urllib2
import re
import requests
import os
import json
import multiprocessing
from multiprocessing import Process, JoinableQueue,Lock ,Queue , Pool , Value
# import Queue

FILE_LOCK =  Lock()
SHARE_Q = multiprocessing.JoinableQueue()  #构造一个不限制大小的的队列
if_exist = 1
# counter.value = 0
counter = Value('i', 0) # int type，相当于java里面的原子变量  

def ensure_dir(f):
	d = os.path.dirname(f)
	if not os.path.exists(d):
		os.makedirs(d)

def ensure_file( f ):
	if not os.path.isfile( f ):
		txt = os.mknod( f )

def get_img_url_num(img_url_list_txt):
	with open(img_url_list_txt , 'r ') as f:
		red = f.read()
		patton = re.compile('(https://.*?)\n')
		img_url_list = re.findall(patton , red)
		return len(img_url_list)

class zhihu_Img_spider(object):
	"""docstring for zhihu_Img_spider"""
	def __init__(self, question_num , url = None , start_offset = 0 ,  img_patton = None):
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
		"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
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
	
		self.start_offset  = start_offset 

		
		# counter.value =  counter.value

		self.img_patton = img_patton

	def get_content(self , url):
		proxies = { "http": "http://10.10.1.10:3128", "https": "http://10.10.1.10:1080", }  
		proxy = {'http': 'http://117.85.105.170:808', 'https': 'https://117.85.105.170:808'}
		r = requests.get( url  , headers = self.headers)# proxies = proxy  )
		cont= r.text 
		# time.sleep(1)
		try:
			txt=json.loads(cont)
			return txt
		except:
			print 'error'

	def get_following(self , content):
		try:
			a = content["paging"]['is_end' ]
	 	except:
			pass	
	 	try:
			for pop in content["data"]:
				x = pop["content"]
				self.following.append( x )
		except:
			print 'error'		
	def saveImg( self , imageURL, mdir = None ,filename=None):
		im = urllib2.urlopen(imageURL , timeout = 5)
		ima = im.read()
		file =  str(mdir) + filename
		f = open(file,'w')
		f.write(ima)
		f.close()

	def Write_file(self , content , mdir = None , filename=None , mode = 'w'):
		file =  str(mdir) + filename
		
		with open(file , mode) as f:
			f.write(content)
		
 
	def get_img_url_list(self):
		with open(self.img_url_list_txt , 'r ') as f:
			red = f.read()
			patton = re.compile('(https://.*?)\n')
			img_url_list = re.findall(patton , red)
			return img_url_list

 
 	def get_following_list(self):
			get_url = self.url + str( self.start_offset ) + "&sort_by=default"
			Con = self.get_content(get_url)

			self.get_following(Con)

	def downloadImg_or_writeFile(self , saveImg = False):
		global if_exist  
		# global counter.value
			
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
					FILE_LOCK.acquire()
					la = str(img_urls[i].split('.')[-1])
					if saveImg:
						self.saveImg(img_urls[i] , mdir = self.dir , filename = str(counter.value) + '.'+ la)
						
						print counter.value, '    ', la

					
					url_write = str(counter.value) + '. ' + str( img_urls[i] ) + '\n'
					self.Write_file(url_write, mdir= self.dir , filename = self.file_name +'.txt' , mode='a')
					counter.value = counter.value +1

					FILE_LOCK.release()
 #---------------------------------------------------------------------------------------------------------------------------------
 #
 #
 #
 #---------------------------------------------------------------------------------------------------------------------------------
class MyProcess(Process):
	def __init__(self , func , *args) :
		super(MyProcess, self).__init__()
 		self.func = func  #传入线程函数逻辑
		self.args = [n for n in list(*args)]

	def run(self):
		self.func(self.args[0] , self.args[1])

def zhihu(ques_code, img_patton= None , offset_here = 0, saveImg = False ):
	global SHARE_Q
    	while not SHARE_Q.empty():

	    	offset_here = SHARE_Q.get() #获得任务
	    	print   offset_here
 		zhu_sp = zhihu_Img_spider( question_num = ques_code  , start_offset = offset_here , img_patton = img_patton)
	 	zhu_sp.get_following_list( )
		zhu_sp.downloadImg_or_writeFile(saveImg=saveImg)	

		# time.sleep(1)
		SHARE_Q.task_done()

if __name__ == '__main__': 
  
	ques_code = 43551423 
	# processes = JoinableQueue()
 	dir = './' + str(ques_code) + '/'
	ensure_dir( dir)

	img_url_list_txt = dir + str(ques_code) + '.txt'
	ensure_file( img_url_list_txt )
	counter.value =  get_img_url_num(img_url_list_txt) + 1

	img_patton = img_patton = re.compile(r'img.*?src="(https:.*?)".*?data-original="(https:.*?)".*?data-actualsrc="(https:.*?)"')

	for index in xrange(0,20,20) :   
		SHARE_Q.put( index )

	pool  = Pool( multiprocessing.cpu_count() )

	for i in xrange(   multiprocessing.cpu_count() ) :
		# process = MyProcess(zhihu , ( ques_code , img_patton ) )
  
 		 pool.apply_async(zhihu , ( ques_code , img_patton ))

 	print 'start'
	pool.close()#关闭进程池，不再接受新的进程
	pool.join()#主进程阻塞等待子进程的退出

	# for process in processes :
	# 	process.join()

	# for process in processes :
	# 	process.terminate()

	SHARE_Q.join()
