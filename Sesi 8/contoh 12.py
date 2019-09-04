# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:26:32 2019

@author: ROG-GL553VD
"""

aList = []

for number in range(1,10):
    aList += [ number ]
    
print ("Nilai aList:",aList)

print ("\nMenampilkan List Menggunakan Iterasi")
for item in aList:
    print (item)

print("\nMenampilkan List Berdasarkan Index")
print("Index  Value")
for i in range(len(aList)):
    print ("%5d %6d" % (i,aList[i]))
    
print("\nMengubah value list")
print("Data List:",aList)
aList[0] = -100
aList[-3] = 199
print("Data List Baru:",aList)