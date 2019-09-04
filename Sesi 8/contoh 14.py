# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:51:57 2019

@author: ROG-GL553VD
"""
#TUPLE
#accessing tuple
tup = (1, 2, 3, 4, 5, 6)
print("tup1[1:5]:",tup[1:5])
print("\n",tup[0])
print("\n",tup[1])
print("\n",tup[-1])
print("\n",tup[-2])
#print("\n",tup[7])

#Updating Values
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
tup3 = tup1 + tup2
print ("\nNilai tup3",tup3)

#Deleting Element
#del tup3[0]

#Deleting Tuple
print("\nBefore Delete",tup3)
del tup3
#print("\nAfter Delete",tup3)

#check element tuple
print("\n",3 in tup1)
print("\n",4 in tup1)