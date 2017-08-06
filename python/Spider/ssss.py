# -*- coding:utf-8 -*-
import urllib2
import re
import requests
import os
import json
import urllib

ss = '<img src="https://pic1.zhimg.com/v2-9de6c33097b0281aeb6c180f1516a4ec_b.png" data-rawwidth="859" data-rawheight="574" class="origin_image zh-lightbox-thumb lazy" width="859" data-original="https://pic1.zhimg.com/v2-9de6c33097b0281aeb6c180f1516a4ec_r.png" data-actualsrc="https://pic1.zhimg.com/v2-9de6c33097b0281aeb6c180f1516a4ec_b.png">'

# img_patton = re.compile(r'img.*?src="(https:.*?)".*?data-original="(https:.*?)".*?data-actualsrc="(https:.*?)"')
# img_patton = re.compile(r'img.*?src="(https:.*?)" .*? data-original="(https:.*?)" ')
# img_patton = re.compile( 'img.*?src="(https:.*?)"' )

img_patton = r'http://[\w\.%=?/\-]+\.(png|jpeg|jpg|jpe|ico|gif)' 
img_urls_truple = re.findall(img_patton, ss)
print img_urls_truple
# img_urls = set()
# for i in img_urls_truple:
# 	for j in i:
# 		img_urls.add(j)
# print len( img_urls) , list(img_urls) , '\n'
# for i in img_urls:
# 	print i