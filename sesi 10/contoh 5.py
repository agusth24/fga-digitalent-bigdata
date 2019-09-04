# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:39:11 2019

@author: ROG-GL553VD
"""
#DataFrame (Cont..)
import pandas as pd

#Create Dataframe (Dict)
print()
data = [
        {'a': 1, 'b': 2, 'c': 3},
        {'e': 10, 'f': 20, 'g': 30}
        ]
df = pd.DataFrame(data)
print (df)

#Create Dataframe (Dict) + Column Index
print()
data = [
        {'a': 1, 'b': 2, 'c': 3},
        {'a': 10, 'b': 20, 'c': 30}
        ]
df = pd.DataFrame(data, index=['first','second'])
print (df)

#Create Dataframe (Dict) + Another DF
print()
data = [
        {'a': 1, 'b': 2, 'c': 3},
        {'a': 10, 'b': 20, 'c': 30}
        ]

#create two column, index and values same as dict keys
df1 = pd.DataFrame(data, index=['first','second'], columns=['a','b'])
#create two column, index and values same as other keys
df2 = pd.DataFrame(data, index=['first','second'], columns=['a','d'])
print (df1)
print (df2)

#Create Dataframe (Dict) Complete
print()
data = {"NIM": pd.Series([1,2,3], index=['a','b','c']),
        "Nama": pd.Series([4,5,6,7], index=['a','b','c','d']),
        "JK": pd.Series([4,5,6,7,8,9], index=['a','b','c','d','e','f'])
        }
df = pd.DataFrame(data)
print(df)
print()
print (df.iloc[1])
print()
print (df.iloc[1,0])
print(df.head())
#access first row dataframe
print()
print(df['NIM'])

#adding new column dataframe
print()
print("Adding new column by passing as series:")
df["Um"] = pd.Series([11,12,13], index=['a','b','c'])
print(df)

print()
print("Adding new column using existing dataframe:")
df["Al"] = df['JK']+df['Um']
print(df)

#deleting column with row name using del funnction
print()
print("Deleting column 'Nama' using DEL Function:")
del df['Nama']
print(df)

#deleting column with row name using POP funnction
print()
print("Deleting row two using POP Function:")
df.pop('NIM')
print(df)

#selection by index label
print()
print (df.loc['b'])

#selection by index number
print()
print (df.iloc[1])
print()
print (df.iloc[1,0])

#add row
print()
df2 = pd.DataFrame([[11,22],[33,44]], columns = ['JK','Um'])
df3 = pd.DataFrame([[55,66],[77,88]], columns = ['JK','Um'])
df = df.append(df2)
df = df.append(df3)
print(df)

print()
print (df.loc[1])

#delete row
print()
df = df.drop('a')
print(df)