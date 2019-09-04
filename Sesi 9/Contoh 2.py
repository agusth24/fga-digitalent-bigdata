# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 13:38:20 2019

@author: ROG-GL553VD
"""

##Fungsi: Pass by reference vs value

#Function definition
def changelist (mylist):
    """This change a passed list into this function"""
    mylist.append([1,2,3,4])
    return print("Values inside the function: ",mylist)

#call function
listoutside = [5,6,7]
changelist(listoutside)
print ("Vlaues outside the function: ",listoutside)