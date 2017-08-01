#coding:utf-8

class HtmlOutputer(object):
	"""docstring for HtmlOutputer"""
	def __init__(self):
		super(HtmlOutputer, self).__init__()
		self.datas = []

	def collect_data(self,data):		
		if data is None:
			return
		self.datas.append(data)

	def outputer_html(self):
		fout = open('out.html','w')
		fout.write('<html>')
		fout.write('<head><meta charset="utf-8"></head>')#告诉浏览器使用什么编码，解决了输出乱码
		fout.write('<body>')
		fout.write('<table>')

		for data in self.datas:
			fout.write('<tr>')
			fout.write('<td>%s</td>' % data['url'].encode('utf-8'))
			fout.write('<td>%s</td>' % data['title'].encode('utf-8'))
			fout.write('<td>%s</td>' % data['summary'].encode('utf-8'))



		fout.write('</table>')
		fout.write('</html>')
		fout.write('</body>')
