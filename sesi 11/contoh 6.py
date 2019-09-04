# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:27:26 2019

@author: ROG-GL553VD
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

# fetch html file
response = urlopen("http://unmul.ac.id/announcements")
html_doc = response.read()

# parse the html file
soup = BeautifulSoup(html_doc, 'html.parser')

# format the parsed html file
strhtm = soup.prettify()

for row in soup.find_all(['h4','a']):
    print(row.get('href'))