# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:35:42 2019

@author: ROG-GL553VD
"""
aList = []
print("Input 10 Bilangan Membuat Histogram")
aList += [ input("Input Bilangan 1:") ]
aList += [ input("Input Bilangan 2:") ]
aList += [ input("Input Bilangan 3:") ]
aList += [ input("Input Bilangan 4:") ]
aList += [ input("Input Bilangan 5:") ]
aList += [ input("Input Bilangan 6:") ]
aList += [ input("Input Bilangan 7:") ]
aList += [ input("Input Bilangan 8:") ]
aList += [ input("Input Bilangan 9:") ]
aList += [ input("Input Bilangan 10:") ]

print("\nMembuan histogram berdasarkan inputan")
print("Index  Value Histogram")
for i in range(len(aList)):
    print ("%5d %6d %s" % (i,int(aList[i]),int(aList[i])*'*'))