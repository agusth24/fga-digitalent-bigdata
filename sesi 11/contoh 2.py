# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 08:55:45 2019

@author: ROG-GL553VD
"""

import pandas as pd
data = pd.read_json("input.json")
print(data)

print()
print (data.loc[[1,3,5],['Salary','Name']])

print()
print(data.to_json(orient="records",lines=True))
