# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 18:04:10 2019

@author: ROG-GL553VD
"""

buah = ["jeruk","apel","mangga","duren"]
#Tambahkan Manggis Dari Belakang

print("Menambahkan List Dari Belakang")
print("List Buah: ",buah)
buah.append("manggis")
print("List buah baru: ",buah)

print()
print("Menambahkan List Dari Depan")
print("List Buah: ",buah)
buah.insert(0,"anggur")
print("List buah baru: ",buah)

print()
print("Menambahkan List Pada Indeks Tertentu")
print("List Buah: ",buah)
buah.insert(2,"duren")
print("List buah baru: ",buah)