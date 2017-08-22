from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.http import Request , Response

res = Request('http://www.w3school.com.cn/example/xmle/books.xml')
fetch(res)
t = Selector(res).xpath('/bookstore/book/title').extract()
print t

# r = Request(url='http://zenofpython.blog.163.com/blog/static/23531705420146124552782')
# fetch(r)