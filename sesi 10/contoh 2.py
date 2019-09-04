# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 18:55:31 2019

@author: ROG-GL553VD
"""

#Pandas
import pandas as pd
import numpy as np

#Empty Series
s = pd.Series()
print(s)

#Create Series [List]
print()
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print(s)

#Create Series + Index [List]
print()
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print(s)

#Create Series [Dict]
print()
data = {'nama' : 'DTS', 'age' : '10', 'sex' : 'W'}
s = pd.Series(data)
print(s)

#Create Series + Index [Dict]
print()
data = {'nama' : 'DTS', 'age' : '10', 'sex' : 'W'}
s = pd.Series(data,index=['b','c','d','a'])
print(s)

#Create Series + Index [Scalar]
print()
s = pd.Series(10,index=[100,101,102,103])
print(s)