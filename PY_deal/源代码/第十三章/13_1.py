#filename urlparse_1.py
from urllib.parse import urlparse, urljoin, urlunsplit
abs_urls = ["http://www.python.org","ftp://www.linux.org","http://www.gtk.org","file://"]
rel_url = "faq.html"

for abs_url in abs_urls:
    url = urljoin(abs_url, rel_url)    #拼合URL
    expected_url = url
    scheme, netloc, path, query, fragment = urlsplit(url) #分解URL
    
    if scheme or scheme == "file":
        print (url,"====> None")
        continue
    
    if scheme is not "ftp":
        expected_url = urlunsplit(('http', netloc, path, query, fragment))
    print (url,"====>",expected_url)
