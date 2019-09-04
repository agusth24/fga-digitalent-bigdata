# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 17:56:07 2019

@author: ROG-GL553VD
"""

list1 = ['physics', 'chemestry', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a","b","c","d"]

print('Accessing Values')
print ("list1[0]:",list1)
print ("list2[1:4]:",list2[1:4])

print()
print('Updating Values')
print ("Value list1[2]:",list1[2])
list1[2]=3000
print ("New Value list1[2]:",list1[2])

print()
print('Deleting Values')
print ("Value list1:",list1)
del list1[2]
print ("New Value list1:",list1)