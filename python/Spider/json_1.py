# -*- coding:utf-8 -*-
import urllib2
import re
import requests
import os
import json
import urllib
 
offset = 0
get_url = ' https://www.zhihu.com/api/v4/members/ji-da-fa-37/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics\
&limit=20&offset=' + str(offset)
# get_url = 'https://www.zhihu.com/api/v4/questions/37787176/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.author.badge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset='+str(offset)
  
follo_headers = {
	"Origin" : "https://www.zhihu.com",
	"Host":"www.zhihu.com",
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
	"Referer" : "https://www.zhihu.com/people/ji-da-fa-37/following",
	 "Accept-Language":"zh-CN,zh;q=0.8",
	"Connection" : "keep-alive",
	"Accept-Encoding":"gzip, deflate, br",
	"authorization":"Bearer Mi4wQUlCQ0pOSHVJQXdBVUFJSlVSSWhEQmNBQUFCaEFsVk43MmVoV1FCbklIYzJIZmoyY2lELWRIdGZxZWlzZ3ZqSDRB|1501158127|bcb9ccfecd888845e2e5d75c110617c33062a836",
}
  
r = requests.get(get_url , headers=follo_headers )
 # r.encoding = 'utf-8'
cont= r.text 
 
# print cont 

txt=json.loads(cont)
# print txt

print txt["paging"]['is_end'],type(txt["paging"]['is_end'])

for pop in txt["data"]:
	print pop["name"]

# req = urllib2.Request(get_url,  headers = follo_headers)
# response=urllib2.urlopen(req)
# res = response.read()
# print res.encode('utf8')
# txt=json.loads(res)
# print txt 

# print u'\u5168\u7403\u7ecf\u5178IT\u6570\u7801\u6392\u884c\u699c'.encode('utf-8')