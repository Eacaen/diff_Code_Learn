# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import Spider , CrawlSpider , Rule
from scrapy.http import Request
from scrapy.selector import Selector

from zhihuImg.items import ZhihuimgItem
import json
import re

class zhihuImg(Spider):
	name = "zhihuImg"
	allowed_domains = ["www.zhihu.com"]
	start_urls = ["http://www.zhihu.com" ]
	# download_delay = 1
	ques_num = str(45729250)
	ques_url =  'https://www.zhihu.com/api/v4/questions/' +  ques_num + '/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&\
	limit=20&offset=0'
	
	ZHIHU_HEADERS = {
	"Origin" : "https://www.zhihu.com",
	"Host":"www.zhihu.com",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
	"Referer" : "https://www.zhihu.com/question/" +  ques_num ,
	 "Accept-Language":"zh-CN,zh;q=0.8",
	"Connection" : "keep-alive",
	"Accept-Encoding":"gzip, deflate, br",
	"authorization":"Bearer Mi4wQUlCQ0pOSHVJQXdBVUFJSlVSSWhEQmNBQUFCaEFsVk43MmVoV1FCbklIYzJIZmoyY2lELWRIdGZxZWlzZ3ZqSDRB|1501158127|bcb9ccfecd888845e2e5d75c110617c33062a836",
	}

	def __init__(self):
		self.headers = self.ZHIHU_HEADERS
		self.img_patton = re.compile(r'img.*?src="(https:.*?)".*?data-original="(https:.*?)".*?data-actualsrc="(https:.*?)"')
	 
		self.ques_num  = str ( self.ques_num )
		
		super(zhihuImg,  self).__init__()

	def start_requests(self):
		yield scrapy.FormRequest( self.ques_url, meta = {'cookiejar': 1}, \
			headers = self.headers, \
			callback = self.parse_item) 

	def parse_item(self, response):
		item = ZhihuimgItem()

		txt = json.loads(response.body)
		for pop in txt["data"]:
			x = pop["content"]

			img_urls_truple = re.findall( self.img_patton , x.encode("utf-8")) 
			print img_urls_truple

			img_urls = set()
			for i in img_urls_truple:
				for j in i:
					img_urls.add(j)

			item['img_url'] = list(img_urls)

			yield item

		next_url = txt["paging"]['next' ]
		if next_url and txt["paging"]['is_end' ] == False:
			yield Request( next_url , headers = self.headers, callback = self.parse_item) 
 