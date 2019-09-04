# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:12:31 2019

@author: ROG-GL553VD
"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = ["Hello World!!"]

print("Length List")
print("Banyak elemen dalam list: ", len(list1))

print()
print("Penggabungan List")
list4 = list1 + list2
print("List4: ",list4)

print()
print("Pengulangan")
print("List4: ",list3 * 2)

print()
print("Membership")
print("Apakah ada angka 3 dalam list:",3 in list1)

print()
print("Iterasi")
for x in list2: print (x)
