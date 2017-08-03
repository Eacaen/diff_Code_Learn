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
		x = pop["content"]
		following.append(x )
		# print x
def saveImg(imageURL,filename=None):
	im = urllib2.urlopen(imageURL)
	ima = im.read()
	file = './zhuhu-img/'+filename
	f = open(file,'w')
	f.write(ima)
	f.close()

# Con = get_content(get_url)
# get_following(Con)

offset = 0
name = 1
while offset < 500:

	get_url = 'https://www.zhihu.com/api/v4/questions/28720296/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Cmark_infos%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B\
	%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset=' + str(offset)

	Con = get_content(get_url)
	get_following(Con)

	offset = offset + 20
	# print offset
	if Con["paging"]['is_end' ]:
		print offset
		break
for i in range(len(following)):

	img_urls = re.findall('img src="(https:.*?)"', following[i].encode("utf-8"))
	# print following[i],type(following[i])
	# print img_urls
	for i in range(len(img_urls)):
		la = str(img_urls[i].split('.')[-1])
		saveImg(img_urls[i], str(name) + '.'+ la)
		name = name+1
		print name, '    ', la