# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 20:06:23 2019

@author: ROG-GL553VD
"""

#Numpy
import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)
a.shape = (3,2)
b = a.reshape(2,3)
print()
print(a)
print()
print(b)

#array attributes jumlah dimensi
a = np.arange(24)
print(a)
print(a.ndim)
b = a.reshape(2,4,3)
print(b)
print(b.ndim)

#itemsize
#int8 1 byte
print()
a = np.array([[1,2,3],[4,5,6]], dtype=np.int8)
print (a.itemsize)

#float32 4 byte
print()
a = np.array([[1,2,3],[4,5,6]], dtype=np.float32)
print (a.itemsize)