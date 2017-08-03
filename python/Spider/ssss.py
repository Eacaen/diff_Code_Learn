# -*- coding:utf-8 -*-
import urllib2
import re
import requests
import os
import json
import urllib

s = u'\u5168\u7403\u7ecf\u5178IT\u6570\u7801\u6392\u884c\u699c'.encode('utf-8')
# print s

reee =  'dwefwf wrefwerg vrwf \
<img src="https://pic2.zhimg.com/v2-1492679bb23923eda0eb29e5f73d4d1d_b.png" \
<img src="//zhstatic.zhihu.com/assets/zhihu/ztext/whitedot.jpg"\
<img src="https://pic2.zhimg.com/v2-1492679bb23923eda0eb29e5f73d4d1d_b.jpg" '

img_urls = re.findall('img src="(https:.*?)"', reee)
print img_urls
print img_urls[1].split('.')[-1]
