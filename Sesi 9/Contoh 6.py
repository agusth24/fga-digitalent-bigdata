# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:35:21 2019

@author: ROG-GL553VD
"""

#Looping
#looping for
for char in 'ilmu komputer':
    print(char)

print()
sum=0
for number in [1,2,3,4,5,6]:
    print(number)
    sum+=number
print("Jumlah angka keseluruhan adalah ",sum)    

#looping while
print()
count = 0
while(count < 5):
    print('Number count is:',count)
    count+=1
else:
    print("End While")

#looping with break
print()
for letter in "programming":
    if letter == "m":
        break
    print("Huruf sekarang:",letter)
print("End For")

#looping with continue
print()
for letter in "programming":
    if letter == "m":
        continue
    print("Huruf sekarang:",letter)
print("End For")