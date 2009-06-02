
# -*- coding: utf-8 -*-
# File feedsig.py
__author__="Sandro Della Giustina (gialloporpora)"
__date__="22 Aug 2007"
__license__="GPL"
__version__="0.0.1"
__URL__="http://www.gialloporpora.netsons.org"
__credits__="http://urltea.com/1apr"

#  How to use ?
# It is necessary to configure a configuration file (for example "config.cfg") adnd executing feedsig.py from commandline with  the configuration file as parameter
# python feedsig.py config.cfg
# Instruction to create the config.cfg file  are available at this link:


# The feed parser module is not included in standard Python packages, download and install it from:
import sys,urllib,feedparser, short



def replace_HTML_character(s):
	s=s.replace("&#039;","'")
	s=s.replace("&apos;","'")
	s=s.replace('&quot;','"')
	s=s.replace('&lt;','<')
	s=s.replace('&gt;','>')
	s=s.replace('&amp;','&')
	s=s.replace('&amp;','&')
	s=s.replace("&nbsp;"," ")
	s=s.replace("&agrave;","a")
	s=s.replace("&egrave;","")
	s=s.replace("&igrave;","")
	s=s.replace("&ograve;","")
	s=s.replace("&ugrave;","")
	s=s.replace("&eacute;","")
	return s
	
def read_config(f):
	file=open(f,"r")
	lines=file.readlines()
	file.close()
	d={}
	#  remove comments lines from config file
	lines=[i for i in lines if i[0:2]!="//"]
	lines=[i.strip("\n") for i in lines]
	params=lines[0].split(",")
	d['filename']=params[0]
	d['type']=d['filename'].split(".")[-1]
	try:
		d['encoding']=params[1]
	except IndexError:
		d['encoding']="utf-8"
	# the second line contains the feeds used for signature
	params=lines[1].split(",")
	d['feed']=[]
	for i in params:
		params2=i.split("\\")
		if (len(params2)==1):params2.append("last")
		d['feed'].append({'url':params2[0],'mode':params2[1]})
	# the last line is optional, it must be inserted only if you want a default  entry in your signature, it is not read from a feed
	try:
		params=lines[2].split(",,")
		if (len(params) ==1): params.append("end")
		d['static_entry']={'content':params[0],'mode':params[1]}
	except IndexError:
		d['static_entry']={'content':"",'mode':"none"}
	return d

def add_feed_signature(feed,type="txt"):
	from random import randrange
	s=""
	for fd in feed:
		x=feedparser.parse(fd['url'])
		if  (fd['mode']=="last"):n=0
		else:  n=randrange(len(x.entries))
		if x.feed!={}:
			title=replace_HTML_character(x.entries[n]["title"])
			link=x.entries[n]["link"]
			if type=="txt":
			 	link=short.getShortUrl(link,'bitly')
			 	s+="*%s* - %s\n" %(title,link)
			else:
			 	s+='<a href="%s">%s</a><br>' %(link,title)
		else:
			s+=short.getShortUrl(fd['url'],'bitly')+"\n"
			errori.append(x.entries.index(i))
	return s

br={'html':"<br/>",'txt':"\n"}
config_file=sys.argv[1]
signature_data=read_config(config_file)
sigfile=open(signature_data['filename'],"w")
firma=""
if (signature_data['static_entry']['mode']=="begin"):
	firma+=signature_data['static_entry']['content']+br[signature_data['type']]
firma+=add_feed_signature(signature_data['feed'] , signature_data['type'])
if signature_data['static_entry']['mode']=="end":
	firma+=signature_data['static_entry']['content']+br[signature_data['type']]
sigfile.write(firma.encode(signature_data['encoding']))
sigfile.close()
