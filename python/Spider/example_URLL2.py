#!/usr/bin/python
#coding=utf-8

import urllib
import urllib2
import cookielib

def post(url, data):
	req = urllib2.Request(url)
	data = urllib.urlencode(data)
	#enable cookie
	cookiefile = "cookiefile"
	cookieJar = cookielib.MozillaCookieJar(cookiefile)
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar));
	response = opener.open(req, data)
	cookieJar.save()
	#print response.read()

	#second http request use cookie
	cookieJar = cookielib.MozillaCookieJar(cookiefile)
	cookieJar.load()
	url = "http://www.xiami.com"
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJar))
	response = opener.open(url)
	print response.read()

def main():
	posturl = "http://www.xiami.com/member/login"
	data = {'email':'myemail', 'password':'mypass', 'autologin':'1', 'submit':'登 录', 'type':''}
	#print post(posturl, data)
	post(posturl, data)

if __name__ == '__main__':
	main()


