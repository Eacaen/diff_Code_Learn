# -*- coding:utf-8 -*-
import urllib2
import re
import requests
import os
import json
import urllib
 
following = [ ]
  
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
 
def get_content(get_url):
	r = requests.get(get_url , headers=follo_headers )
	cont= r.text 
	txt=json.loads(cont)
	return txt

def get_following(content):
	for pop in content["data"]:
		following.append( pop["name"])
		# print pop["name"]

# Con = get_content(get_url)
# get_following(Con)

offset = 0
while 1:

	get_url = ' https://www.zhihu.com/api/v4/members/ji-da-fa-37/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics\
	&limit=20&offset=' + str(offset)

	Con = get_content(get_url)
	get_following(Con)

	offset = offset + 20
	if Con["paging"]['is_end' ]:
		break
for i in range(len(following)):
	print i+1,'. ', following[i]
# print Con["paging"]['is_end' ],Con["paging"]['totals' ]