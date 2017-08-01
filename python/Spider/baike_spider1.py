from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html,"lxml")
print soup.prettify()
print soup.title
print soup.head
print soup.p
print soup.p.attrs
print soup.p.string
print '---------------------------------\n'
print soup.a
print soup.a.string
print type(soup.a.string)

print soup.p.contents
print soup.p.string

print soup.html.string
print '---------------------------------\n'

# for string in soup.strings:
#     print(repr(string))

print soup.find_all('a')
print '-----------------------------\n'
import re
for tag in soup.find_all(re.compile('^b')):
	print tag.name

# print soup.find_all(id='link1')
print soup.find_all("a", class_="sister")

for i in range(1,6):
	print i