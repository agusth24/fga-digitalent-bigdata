# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:01:30 2019

@author: ROG-GL553VD
"""

a=27
b=27

#Operator Arithmetic
print("Arithmetic '+' :",a+b)
print("Arithmetic '-' :",a-b)
print("Arithmetic '*' :",a*b)
print("Arithmetic '/' :",a/b)
print("Arithmetic '**' (Pangkat) :",a**b)
print("Arithmetic '//' (Div) :",a//b)
print("Arithmetic '%' (Mod) :",a%b)

print()

#Operator Comparison
print("Comparison '>' :",a>b)
print("Comparison '<' :",a<b)
print("Comparison '==' :",a==b)
print("Comparison '!=' :",a!=b)
print("Comparison '>=' :",a>=b)
print("Comparison '<=' :",a<=b)

print()

#Operator Assignment
b = 4
b = a
print("Assignment '=' :",b)
b = 4
b += a
print("Assignment '+=' :",b)
b = 4
b -= a
print("Assignment '-=' :",b)
b = 4
b *= a
print("Assignment '*=' :",b)
b = 4
b /= a
print("Assignment '/=' :",b)
b = 4
b **= a
print("Assignment '**=' :",b)
b = 4
b //= a
print("Assignment '//=' :",b)
b = 4
b %= a
print("Assignment '%=' :",b)