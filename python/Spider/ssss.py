# -*- coding:utf-8 -*-
import urllib2
import re
import requests
import os
import json
import urllib

def jj():
	for i in range(10):
		yield i

d = jj()
print d , type(d)
# print d.next()
for i in d:
	print i