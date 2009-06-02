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