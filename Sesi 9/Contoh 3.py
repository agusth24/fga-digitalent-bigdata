# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 13:58:33 2019

@author: ROG-GL553VD
"""

#Function Argumen
#Required argument
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return;

#call function printme
printme('Hello World!!')

print()
#keyword argument
def myid(name,age):
    "This prints a passed string into this function"
    print("Name: "+name+"\nAge :"+str(age))
    return;

#call function myid
myid(age=50,name='dts')
myid('dts',50)

print()
#default argument
def myid_2(name,age=50,sex='P'):
    "This prints a passed string into this function"
    print("Name: "+name+"\nAge :"+str(age)+"\nSex :"+str(sex))
    return;

#call function myid
#myid_2(age=37,name='DTA-1')
#myid_2(name='DTA-2')
myid_2(name='DTA-2',sex='L')

#variable-length arguments
def print_me_again(key1, *keys2):
    "This prints a passed string into this function"
    print ("Output arguments: ")
    print(key1)
    for row in keys2:
        print(row)
    return;

#call print_me_again
print_me_again(10)
print_me_again(10,2,3,4,5,6)