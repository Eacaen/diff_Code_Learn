# -*- coding:utf-8 -*-
import re
import requests
import urllib2
import urllib
import re
import cookielib
session = requests.Session()

headers = {

    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0",
    "Host" : "www.zhihu.com" ,
    "Cookie" : 'q_c1=294db7988df848439c79641bb1425410|1500683095000|1500683095000; q_c1=94f9bc450095470c9ace44beac3d7174|1500683095000|1500683095000; _zap=5140e685-216a-4751-8f08-a261bd0ce0c4; r_cap_id="MGY4ZDdkOWQzYjNlNDM3MWI3MGNhOTE2NzY2YjRhZmQ=|1501257852|e0dd03726c26d314bddb5595c76a1e2c56bfdf79"; cap_id="OGNjNjk4MWUyMjJkNDA1NWI3ZjNkYzg1MGZkZmZjZWY=|1501257852|18060184992be06b7e73b6df72617a2d450df4d9"; d_c0="AJCCJPVtHwyPTuYz0y9k-vcizLhmABRoSnw=|1501047629"; __utma=51854390.1097849395.1501047632.1501225294.1501248816.6; __utmz=51854390.1501248816.6.3.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.000--|2=registration_date=20170727=1^3=entry_date=20170722=1; aliyungf_tc=AQAAAKRZCk/3qAQAkwvCemrZgbsKHgJx; _xsrf=38d3ebaee5feee39f071f9f561fb4c53; __utmc=51854390; _xsrf=38d3ebaee5feee39f071f9f561fb4c53; l_cap_id="Y2U1NWU0ZjEyNjhmNDE1MGI3MTVmNTEzY2ViNDIxYjA=|1501257852|883810cf70ca3d99c61d80c75a52a9309c83a4c2"',
    "Referer" : "https://www.zhihu.com/",


}

def getToken():
	html = session.get("https://www.zhihu.com" , headers = headers)
	pattern = re.compile(r'<input type="hidden" name="_xsrf" value="(.*?)"/>')

 	authenticity_token = pattern.findall(html.content)[0]
 	print authenticity_token
 	return authenticity_token

log_data = {
"_xsrf":	getToken(),
"password":	"119110315",
"captcha_type":	"cn",
"phone_num":	"13152418529"
# 'remember_me': 'true'  
}

logUrl = 'https://www.zhihu.com/login/phone_num'

r = session.post(logUrl , data=log_data, headers=headers)

print r.status_code
print r.text

af_log = "https://www.zhihu.com/roundtable"
aca = "https://www.zhihu.com/people/eacaen/activities"
exp = "https://www.zhihu.com/explore"
response = session.get(exp ,  headers=headers)
print(response.content)

# for key,value in response.cookies.items():
#     print(key+"="+value)



# r = session.get(af_log , headers=headers)
# print r.text

# req = urllib2.Request(, data=log_data, headers=headers)
# res = urllib2.urlopen(req)
# print res.read()

 
 
 
 