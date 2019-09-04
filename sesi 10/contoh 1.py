# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 18:27:59 2019

@author: ROG-GL553VD
"""
#Open File n Read
f = open("test.txt", 'r')
#print(f.read(10))
#print(f.read(14))
print(f.read())

#Create File and Read
print()
with open("test2.txt", "w") as f:
    f.write("This new first line\n")
    f.write("This new second line\n")
    f.write("This new third line\n")
f = open("test2.txt")
print(f.read())

#Create/Append Content and Read
print()
with open("test2.txt", "a") as f:
    f.write("This new fourth line\n")
    f.write("This new fifth line\n")
    f.write("This new sixth line\n")
f = open("test2.txt")
print(f.read())

#Read file gambar
print()
f = open("TOR Aplikasi Sistem SPPD 2018.docx","r+b")
print(f.read())

#Exception Handling
print()
try:
    f = open("test.txt")
    print(f.read(10))
    print(f.read(14))
    print(f.read(2000))
finally:
    f.close()
    
    