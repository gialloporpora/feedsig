You can read this file at this URL: http://wiki.github.com/gialloporpora/feedsig

**Welcome to the FeedSig Wiki**

This is a little Python script to change email signature using randomized phrases or entry from feeds, for example if you are registered to Last.fm you can use your personal feed to show in your  email signature the song you are listening, or, if you are registered to Twitter you can show  your latest tweet in your signature.


h2. Installation

First of all you need to install two Python modules: **feedparser** and **simplejson**:

* "FeedParser":http://www.feedparser.org/
* "SimpleJson":http://pypi.python.org/pypi/simplejson/

If you have **"SetupTools":http://pypi.python.org/pypi/setuptools**  installed, you can install simplejson in this way:

* *$** __easY_install simplejson__
* **$** __easy_install feedparser__

These are all required modules. 

To install (for the moment I have no created an install script) simply unpack the files in a folder.

h2. The files

* **short.py** - This is a library that uses shortener Url services to shorten long url in text signatures. For the moment the supported services are: **Bit.ly**, **Tinyurl.com** and **Snipurl.com**
* **feedsig.py** - is the file that contains the code to update your signature file
* **sigconfig.py** - this is the default file where are saved your signature settings. It was created using the __EXAMPLE__ data  defined in **feedsig.py**
* **readme.txt** - It contains the info that are reported in this Wiki page
* **feedsig.bat** - BAT executable file that update your signature by running the script. 

h2. How to create your own signatur

To create your signature setting you have two ways:

# Edit the file **sigconfig.json** with a text editor like **"Crimson Editor":http://www.crimsoneditor.com/**
# From Python console import the module **feedsig** and create a data settings. It is a dictionary or a list of dictionaries. An example of this type of data structure is the EXAMPLE data in **feedsig.py**

For example, to create the **sigconfig.json** file in this archive I have used these lines of code:

** >>> import feedsig**
** >>> feedsig.writeConfigFile(feedsig.EXAMPLE)**

For more info about data settings, see [[Data settings for your signature]]

h2. Usage

To update your signature you can run the  script **feedsig.py** directly or using the **feedsig.bat** file on Windows. I think the better way is to create a shortcut in your desktop or - as I like - using **"Executor":http://lifehacker.com/400566/executor-is-impressive-full+featured-app-launcher** or other similar launcher as **"Enso":http://www.humanized.com/enso/** or **"Launchy":http://www.launchy.net/**. 

By default the  script use the file **sigconfig.json** for reading settings, if you to use another configuration file, run:

**python feedsig.py filename.json**

with an additional filename as parameters.

**Good Luck!**



================================================

h2. Setting your own signature

To  config your signature you could edit the **sigconfig.json** with a text editor or using python

The data is a dictionary (or a list of dictionaries for more than one signature)  with this specification:

* **global** is a dictionary containing global setting for your signature (**required**)
* **feed** - it is a dictionary (or a list of dictionaries) that indicates  the feeds to get informations (**optional**)
* **static_entry** - it is a dictionary containing simple text to  add at your signature, it could be added before the dinamic test from  feed, or after

h2. Global settings

The **global** dictionary have these keys, all values are simple string:

* **filename** - the signature filename. The file extension must be **txt** if you compose in plain-text, **html** if you compose mail in HTML (**required**)
* **encoding** - The charset encoding of your outgoing mail, by default **utf-8** (**optional**)

h2. feed

It is a dictionary (or a list of dictionaries) that contains info about feed to parse for getting dinamical entry in your signature. These are keys for dictionary:

* **url** - The url of the feed. (**required**)
**mode** it could be  be assume the value **random** if you want to get a random entry for your feed instead of the most recent one (**optional**)

h2. static_entry

This is a dictionary that contains static text phrases, this text phrases could be added before of after the feed entry part.  This dictionary have two keys:

* **content** - a string (or a list of string) to insert  in your signature. If you put a list of string, one of them will be randomically added  in your signature. (**required**)
* **mode** - You can set this key to **begin** for inserting the  text before feeds text part, by default the text will be added  after the feed part. (**optional**)


**feed** and **static_entry** are optional but to have sense you must specify one of them in your setting otherwise  you will obtain an empty signature.

h2. Saving your setting  in a file

**>>> import feedsig**
**>>> d={[ your data  }] # look to the **feedsig.EXAMPLE** for an example**
**>>> feedsig.writeConfigFile(d)**






