# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:40:57 2019

@author: ROG-GL553VD
082199188429"""

a = 0
genap = 0
total = 0

while (a<=10):
    a+=1
    
    if(a%2 == 0):
        #genap=a
        #total=total+genap
        total += a
print(total)