import urllib2
class HtmlDownloader(object):
	"""docstring for HtmlDownloader"""
	def __init__(self):
		super(HtmlDownloader, self).__init__()
		print 'ddddddd'
	def download(self,url):
		if url is None:
			return None

		response = urllib2.urlopen(url)
		# print response.read()

		if response.getcode() != 200:
			print 'download fail'
			return None
		
		return response.read()

if __name__=='__main__':
	dd = HtmlDownloader()
	root_url = "http://baike.baidu.com/item/Python"
	dd.download(root_url)