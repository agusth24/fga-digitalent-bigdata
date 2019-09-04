# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:32:43 2019

@author: ROG-GL553VD
"""

#Decision Making
nilai = int(input("Nilai mata kuliah "))
if(nilai >= 80 ):
    print ("Bobot Nilai A")
elif(nilai >= 70):
    print ("Bobot Nilai B")
elif(nilai >= 60):
    print ("Bobot Nilai C")
elif(nilai >= 50):
    print ("Bobot Nilai D")
else:
    print ("Bobot Nilai E")