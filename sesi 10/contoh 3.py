# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:03:05 2019

@author: ROG-GL553VD
"""

#access first element
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print (s[0])

#access 3 element
print()
print (s[:3])

#access last 3 element
print()
print (s[-3:])

#access with index
print()
print (s[['a','c','d']])
#print (s['f'])

