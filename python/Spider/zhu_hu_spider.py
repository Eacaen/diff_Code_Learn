# -*- coding:utf-8 -*-
import urllib2
import urllib
import re
import cookielib


def get_xsrf():
	req = urllib2.urlopen("https://www.zhihu.com")
	html_zhihu = req.read()
	patton_xsrf = re.compile('<input type="hidden" name="_xsrf" value="(.*?)"/>')
	_xsrf = re.findall(patton_xsrf , html_zhihu)[0]
 	return _xsrf

data = {
"_xsrf":	get_xsrf(),
"password":	"119110315",
"captcha_type":	"cn",
"phone_num":	"13152418529"
# 'remember_me': 'true'  
}

header = {  
'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0',  
'Host':'https://www.zhihu.com',  
"Referer" : "https://www.zhihu.com/",
"Cookie" : ' q_c1=294db7988df848439c79641bb1425410|1500683095000|1500683095000; q_c1=94f9bc450095470c9ace44beac3d7174|1500683095000|1500683095000; _zap=5140e685-216a-4751-8f08-a261bd0ce0c4; r_cap_id="Y2NlNzBkM2RkNDRhNDhhNzkyMDJjODA1ODM3ZDNiZTc=|1501248814|b616d106c716b3061c9d788428672b8c5a6f9c15"; cap_id="ODg5ZWJkMTljY2UwNDc4NmFiMDA5YmY2NDFiNGFkMzY=|1501248814|859cb460340681bfd7c506c74ca383f3230b53be"; d_c0="AJCCJPVtHwyPTuYz0y9k-vcizLhmABRoSnw=|1501047629"; __utma=51854390.1097849395.1501047632.1501225294.1501248816.6; __utmz=51854390.1501248816.6.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.000--|2=registration_date=20170727=1^3=entry_date=20170722=1; aliyungf_tc=AQAAAKRZCk/3qAQAkwvCemrZgbsKHgJx; _xsrf=38d3ebaee5feee39f071f9f561fb4c53; __utmc=51854390; _xsrf=38d3ebaee5feee39f071f9f561fb4c53; l_cap_id="NTVlYzUxNTU4NjRhNDJiMTg2MzQ1MDU2Njc2YjdjMTU=|1501248814|4c9527c1678cd4d8a2748738e324a0fa8bc595e6"; __utmb=51854390.0.10.1501248816'
}

url = 'https://www.zhihu.com/login/phone_num'
# url_data = urllib.urlencode(data).encode('utf-8')

req = urllib2.Request(url , header)  
data = urllib.urlencode(data)  
#enable cookie  
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
response = opener.open(req, data)  

print response.getcode()
print response.read()

# response = urllib2.urlopen("https://www.zhihu.com/people/eacaen/following/topics")

# print response.getcode()
# print response.read()


#初始化一个CookieJar来处理Cookie
# cookieJar=cookielib.CookieJar()
# cookie_support = urllib2.HTTPCookieProcessor(cookieJar)
# #实例化一个全局opener
# opener=urllib2.build_opener(cookie_support)
# request = urllib2.Request(url, url_data, headers)
# result=opener.open(request)
# print result.read()

# dd = "https://www.zhihu.com/people/eacaen/following/topics"
# page =opener.open(dd)
# content = page.read().decode('utf-8')
# print(content)