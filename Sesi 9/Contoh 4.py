# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 14:22:13 2019

@author: ROG-GL553VD
"""

#Global vs Local Variable
total = 0 #Global Variable
def sum_number(number1, number2):
    total = number1 + number2 #Local Variable
    print ("Inside the function local total: "+str(total))
    return total;

# call sum_number
sum_number(30, 233)
print ("Outside the function global total:"+str(total))
total = sum_number(20,50)
print ("Outside the function global total from total local:"+str(total))