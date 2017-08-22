from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from scrapy.http import Request

res = Request('http://www.w3school.com.cn/example/xmle/books.xml')
print res

body = "<html><head>\
  <base href='http://example.com/' />\
  <title>Example website</title>\
 </head>\
 <body>\
  <div id='images'>\
   <a href='image1.html'>Name: My image 1 <br /><img src='image1_thumb.jpg' /></a>\
   <a href='image2.html'>Name: My image 2 <br /><img src='image2_thumb.jpg' /></a>\
   <a href='image3.html'>Name: My image 3 <br /><img src='image3_thumb.jpg' /></a>\
   <a href='image4.html'>Name: My image 4 <br /><img src='image4_thumb.jpg' /></a>\
   <a href='image5.html'>Name: My image 5 <br /><img src='image5_thumb.jpg' /></a>\
   <a href='ima5.html'>Name: My image 5 <br /><img srcc='image6_thumb.jpg' /></a>\
  </div></body></html>"

t = Selector(text=body).xpath('//head/base/@href').extract()
t = Selector(text=body).xpath('//body/div/a/text()').extract()
print t
