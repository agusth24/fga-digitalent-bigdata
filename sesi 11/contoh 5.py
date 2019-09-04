# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:27:26 2019

@author: ROG-GL553VD
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

# fetch html file
response = urlopen("https://www.tutorialspoint.com/python/python_overview.htm")
html_doc = response.read()

# parse the html file
soup = BeautifulSoup(html_doc, 'html.parser')

# format the parsed html file
strhtm = soup.prettify()

# print the first few char
print(strhtm[:255])

print(soup.title)
print(soup.title.string)
print(soup.a)
print(soup.a.string)
print(soup.img)
print(soup.b)
print(soup.b.string)

for row in soup.find_all('b'):
    print (row.string)