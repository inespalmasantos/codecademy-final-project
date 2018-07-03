'''
Python module to fetch text data from the web
and remove any non-text data from it
'''

import urllib2
response = urllib2.urlopen("https://www.gutenberg.org/files/1661/1661-h/1661-h.htm")
html = response.read()
