# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:12:47 2019

@author: ROG-GL553VD
"""

import pandas as pd
data = pd.read_excel("input.xlsx")
print(data)

print()
print (data.loc[[1,3,5],['salary','name']])

with pd.ExcelFile("input.xlsx") as excel:
    df1 = pd.read_excel(excel, "data1")
    df2 = pd.read_excel(excel, "data2")
    
print("#### Sheet1 ####")
print(df1[0:5]['salary'])
print("#### Sheet2 ####")
print(df2)      