# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 08:04:26 2019

@author: ROG-GL553VD
"""

import pandas as pd
data = pd.read_csv("D:\AppInstalled\input.csv",";")
print(data)

print()
print (data[0:5]['NIM'])

print()
print (data.loc[:,['NAMA','NIM','PROGRAM_STUDI']])

print()
print (data.loc[[1,3,5],['NAMA','NIM']])


print()
print (data.loc[2:11,['NAMA','NIM']])