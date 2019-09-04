# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:08:32 2019

@author: ROG-GL553VD
"""

#DataFrame
import pandas as pd

#Empty Dataframe
df = pd.DataFrame()
print(df)

#Create Dataframe (List)
print()
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print (df)

#Create Dataframe (List) + Column Name
print()
data = [['Alex',10,'W'],['Bob',12,'M'],['Clarke',13,'M']]
df = pd.DataFrame(data,columns=["Name","Age","Sex"],dtype=float)
print(df)

#Create Dataframe (Dict) + Column Name
print()
data = {"Name":["Tom","Jack","Steve","Ricky"],"Age":[23,45,21,32]}
df = pd.DataFrame(data)
print(df)

#Create Dataframe (Dict) + Column Name + Index Name
print()
data = {"Name":["Tom","Jack","Steve","Ricky"],"Age":[23,45,21,32]}
df = pd.DataFrame(data,index=["data_1","data_2","data_3","data_4"])
print(df)