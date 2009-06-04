
import urllib

SUPPORTED_SHORTENER_SERVICES=["bitly", "snipurl", "snipurl"]

class ShortUrlTemplate(object):
	def __init__(self, name, APIurl, params,method='get'):
			self.name=name
			self.APIurl=APIurl
			self.params=params
			self.method=method

	def getResponse( self ):
		params=urllib.urlencode(self.params)
		if self.method=="post":
			f=urllib.urlopen(self.APIurl, params)
		else: f=urllib.urlopen(self.APIurl+"?"+params)
		s=f.read()
		f.close()
		return s
		
	def getShortUrl(self, urlToShorten):
		pass
		
class tinyurl(ShortUrlTemplate):
	def __init__(self):
		ShortUrlTemplate.__init__(self, "tinyurl", "http://tinyurl.com/api-create.php", {"url" : "http://www.google.com"})
	def getShortUrl(self, urlToShorten):
		self.params["url"]=urlToShorten
		return self.getResponse()

class bitly(ShortUrlTemplate):
	def __init__(self):
			ShortUrlTemplate.__init__(self, "bit.ly", "http://api.bit.ly/shorten", {"version" : "2.0.1","login" : "gialloporpora", "apiKey"  : "R_d7b1cb733163eff7887128b54d51eb79", "longUrl" : "http://www.google.com" } )
	def getShortUrl(self, urlToShorten):
		import simplejson
		self.params["longUrl"]=urlToShorten
		response=simplejson.loads(self.getResponse())
		return response["results"][unicode(self.params["longUrl"])]["shortUrl"]
class snipurl(ShortUrlTemplate):
	def __init__(self):
		ShortUrlTemplate.__init__(self, "snipurl", "http://snipurl.com/site/getsnip", {"sniplink" : "http://www.snipurl.com", "snipuser" : "gialloporpora",  "snipapi" : "729d262e9e0f119431570b29eff5a484"}, "post")	
		
	def getShortUrl(self, urlToShorten):
		import re
		self.params["sniplink"]=urllib.quote(urlToShorten)  # this is strange for me to quote, arguments are automatically quoted by url
		regex=re.compile("<id>([^<]+)</id>")
		s=self.getResponse()
		return regex.search(s).group(1).replace("snipurl.com","sn.im")

def getShortUrl(urlToShorten, service="bitly"):
	""" 
	This function accept as input an URL and an  Shortener service.
	By default, if no service is passed to function, it uses the bit.ly service to short urls.
	Possible values for service are: 'bitly' (default), 'tinyurl', 'snipurl'
	"""
	if service=='tinyurl': shorturl=tinyurl()
	elif service=='snipurl': shorturl=snipurl()
	else: shorturl=bitly()
	return shorturl.getShortUrl(urlToShorten)