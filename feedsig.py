# -*- coding: utf-8 -*-
# File feedsig.py
__author__="Sandro Della Giustina (gialloporpora)"
__date__="02 Jun 2009"
__license__="GPL"
__version__="1.0"
__URL__="http://www.gialloporpora.netsons.org"

# For documentation on using this script to change your email signature see the readme.txt file



# The feed parser module is not included in standard Python packages, download and install it from: http://www.feedparser.org/

# EXAMPLE is a default setting, you could look at it to see how script works. EXAMPLE is stored in sigconfig.json file



EXAMPLE=[{}, {}]
EXAMPLE[0]["global"]={"filename" : "d:\\firme\\firma.txt"}
EXAMPLE[0]["feed"]=[{"url" : "http://feeds.feedburner.com/IlBlogCheNonC", "mode" :"random"}, {"url" : "http://twitter.com/statuses/user_timeline/1320531.rss"}]
EXAMPLE[0]["static_entry"]={"content" : ["Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. ", "There are only 10 types of people in the world: Those who understand binary, and those who don't", "God created the natural number, and all the rest is the work of man", " Give me a place to stand, and I will move the earth.", "To divide a cube into two other cubes, a fourth power or in general any power whatever into two powers of the same denomination above the second is impossible, and I have assuredly found an admirable proof of this, but the margin is too narrow to contain it."]}
# This define an HTML signature
EXAMPLE[1]["global"]={"filename" : "d:\\firme\\firma.html", "encoding" : "utf-8"}
EXAMPLE[1]["feed"]=[{"url" : "http://ws.audioscrobbler.com/1.0/user/gialloporpora/recenttracks.rss", "mode" : "random"}]
EXAMPLE[1]["static_entry"]={"content" : ["Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. ", "There are only 10 types of people in the world: Those who understand binary, and those who don't", "God created the natural number, and all the rest is the work of man", "Give me a place to stand, and I will move the earth.", "To divide a cube into two other cubes, a fourth power or in general any power whatever into two powers of the same denomination above the second is impossible, and I have assuredly found an admirable proof of this, but the margin is too narrow to contain it."] }


# Required packages not available with default Python distributions:
# simplejson: 
# feedparser: 

import re, sys,urllib,feedparser, simplejson, short
from random import randrange
from types import ListType


# In this dictionary are stored signature settings



def writeConfigFile(d, f="sigconfig.json"):
	"""
	Create a json file to store your signature settings.
	d - is an dictionary
	f - a filename (string)
	"""
	f=open(f,"w")
	simplejson.dump(d, f, indent=2)
	f.close()

def unescape(string):
	""" 
	Unescap special HTML characters as &amp;;, &nbsp;, &acute; ecc...
	Original code: http://snippets.dzone.com/posts/show/4569
	"""
	from htmlentitydefs import name2codepoint as n2cp
	def substitute_entity(match):
		ent = match.group(3)
		if match.group(1) == "#":
			# decoding by number
			if match.group(2) == '':
				# number is in decimal
				return unichr(int(ent))
			elif match.group(2) == 'x':
				# number is in hex
				return unichr(int('0x'+ent, 16))
		else:
			# they were using a name
			cp = n2cp.get(ent)
			if cp: return unichr(cp)
			else: return match.group()
	
	entity_re = re.compile(r'&(#?)(x?)(\w+);')
	return entity_re.subn(substitute_entity, string)[0]
	
def readConfigFromFile(f="sigconfig.json"):
	f=open(f,"r")
	data=simplejson.load(f)
	f.close()
	return data

def add_feed_signature(feed,type, shortenerService):
	s=""
	for fd in feed:
		x=feedparser.parse(fd["url"])
		# if x: raise IOError("Unable to get feed, feed could be unavailable or you could have network connection problem")	
		if  not(fd.has_key("mode")): fd["mode"]="last"
		if  (fd["mode"]=="last"):n=0
		else:  n=randrange(len(x.entries))
		if x.feed!={}:
			title=unescape(x.entries[n]["title"])
			link=x.entries[n]["link"]
			if type=="txt":
			 	link=short.getShortUrl(link,shortenerService)
			 	s+="*%s* - %s\n" %(title,link)
			else:
			 	s+='<a href="%s">%s</a><br>' %(link,title)
	return s

def createSignature(data):
	import types
	if not(type(data)==ListType): data=[data]
	for i in data:
		writeSignatureFile(i)

def writeSignatureFile(d):
	"""
	It accept a dictionary as input and write the signature in a specified file
	For documentation about dictionary keys and values see the example_config dictionary or sigfile=open(d["global"]["ilename"],"w") the readme.txt file
	"""
	import types
	sigtype=d["global"]["filename"].split(".")[-1]
	br={'html':"<br/>",'txt':"\n"}
	sigfile=open(d["global"]["filename"],"w")
	signature=""
	if d.has_key("static_entry"):
		if not(d["static_entry"].has_key("mode")):  d["static_entry"]["mode"]="end"
		if type(d["static_entry"]["content"])==ListType: staticentry=d["static_entry"]["content"][randrange(len(d["static_entry"]["content"]))]
		else: staticentry=d["static_entry"]["content"]
		if d['static_entry']['mode']=="begin" :
			signature+=staticentry+br[sigtype]
		if not(d["global"].has_key("shortenerService")): d["global"]["shortenerService"]='bitly'
	if d.has_key("feed"): signature+=add_feed_signature(d['feed'] , sigtype, d["global"]["shortenerService"])
	if d.has_key("static_entry"):
		if d["static_entry"]["mode"]=="end":
			signature+=staticentry+br[sigtype]
		if not(d["global"].has_key("encoding")): d["global"]["encoding"]="utf-8"
	sigfile.write(signature.encode(d["global"]["encoding"]))
	sigfile.close()



if __name__ == "__main__":
	if len(sys.argv)>2: config_file=sys.argv[1]
	else: config_file="sigconfig.json"
	d=readConfigFromFile(config_file)
	createSignature(d)