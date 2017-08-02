import re
import requests
import urllib2
import urllib
import cookielib
s = 'fewf<a href="/people/hehe-eacaen" target="_blank" class="UserLink-link">hehe Eacaen</a>'


patton_xsrf =  re.compile('<a href="/people/(.*?)" target="_blank" class="UserLink-link">(.*?)</a>')
_xsrf = re.findall(patton_xsrf , s)
c = _xsrf[0]
print c
h1 = "https://www.zhihu.com/people/"
h2 = "/following"
h3 = h1+str(c)+h2

print h3


