# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 19:18:48 2019

@author: ROG-GL553VD
"""

#DICTIONARY
#Accessing List
countSe = {'Nama':'DTS','Umur':'8','Class':'Big Data'}
print(countSe)
print("\ndict['Nama']",dict['Nama'])
print("\ndict['Class']",dict['Class'])

#print("\ndict['Alamat']",dict['Alamat'])

#Updating Dictionary
dict['Umur'] = '9'
dict['Class'] = 'Cloud Computing'
dict['Alamat'] = 'Universitas Mulawarman'
print(dict)

#Remove Element, Clear Element, Del Dict
del dict['Nama']
print(dict)
dict.clear()
print(dict)
del dict
#print(dict)

