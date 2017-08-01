# -*- coding:utf-8 -*-
import re
import requests
import urllib2
import urllib
import re
import cookielib
session = requests.Session()

header = {
"Accept" : "text/html,application/xhtml+x…lication/xml;q=0.9,*/*;q=0.8" ,
"Accept-Encoding"   : "gzip, deflate, br",
"Accept-Language"   : "en-US,en;q=0.5",

"Connection"	: "keep-alive",
"Cookie"	: "logged_in=no; _octo=GH1.1.1970970484.1500426888; _ga=GA1.2.1727967677.1500426888; _gh_sess=eyJsYXN0X3dyaXRlIjoxNTAxMjMyMzg5MDEyLCJzZXNzaW9uX2lkIjoiZThiNTIxZmFhYjdiNWMzZTVjNTY2YWY4MmU5MWJjNWQiLCJjb250ZXh0IjoiLyIsImxhc3RfcmVhZF9mcm9tX3JlcGxpY2FzIjoxNTAxMjMyMzkyMTEzLCJyZWZlcnJhbF9jb2RlIjoiaHR0cHM6Ly9naXRodWIuY29tLyIsIl9jc3JmX3Rva2VuIjoiQ2JkYjAxSGREZTVtcnJZU29GQ29aYzNabHZjWitCQmN6WFdKcDEwV2thaz0iLCJmbGFzaCI6eyJkaXNjYXJkIjpbXSwiZmxhc2hlcyI6eyJhbmFseXRpY3NfbG9jYXRpb25fcXVlcnlfc3RyaXAiOiJ0cnVlIn19fQ%3D%3D--59c4346f810a2bd6b496962bda680907c92ba032; tz=Asia%2FShanghai; _gat=1",
 
"Host"  : "github.com" ,
"Upgrade-Insecure-Requests" : "1",  
"User-Agent"	:"Mozilla/5.0 (X11; Ubuntu; Lin… Gecko/20100101 Firefox/54.0" ,

"Content-Type"   : "application/x-www-form-urlencoded",
# "Content-Length"  : "182",
"Referer"	: "https://github.com",
}
def get_authenticity_token():
	req = urllib2.urlopen("https://github.com/login")
	html_git = req.read()
	pattern = re.compile(r'<input name="authenticity_token" type="hidden" value="(.*)" />')
	_authenticity_token = re.findall(pattern , html_git)[0]
 	return _authenticity_token

def getToken():
	html = session.get('https://github.com/login', headers=header)
	pattern = re.compile(r'<input name="authenticity_token" type="hidden" value="(.*)" />')
	# print html.content
	authenticity_token = pattern.findall(html.content)[0]
 	return authenticity_token

log_data = {
"commit" : "Sign+in",
"utf8" :	"✓",
# 'utf8': '%E2%9C%93',
"authenticity_token" :	getToken(),
"login" :	"Eacaen",
"password" :	"HTy119110315"	
}
 
logUrl = "https://github.com/session"
# r = session.post(logUrl, data=log_data, headers=header)
# print r.status_code
  

req = urllib2.Request(logUrl ,  headers=header )  
data = urllib.urlencode(log_data)  
#enable cookie  
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
# response = opener.open(req, data)  
response = urllib2.urlopen(req , data)

print response.getcode()
print response.read()