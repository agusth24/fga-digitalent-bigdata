# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 15:13:14 2019

@author: ROG-GL553VD
"""

#OOP

class Employee: #class
    "Common base class for all employes"
    employee_count = 0 #global_attribute
    
    def __init__(self, name, salary): #method_constructor
        self.name = name #local_attribute
        self.salary = salary #local_attribute
        Employee.employee_count += 1
    
    def displayCountEmployee(self): #method
        print("Total employee %d" % Employee.employee_count)
    
    def displayEmployee(self): #method
        print ("Name: ",self.name,", Salary: ",self.salary)

#call class + object
print("Input first employee")
emp1 = Employee("Zara",2000) #object
print("Input second employee")
emp2 = Employee("Manni",5000) #object

print()
#access object
emp1.displayEmployee()
emp2.displayEmployee()

emp1.displayCountEmployee()
emp2.displayCountEmployee()