# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 15:56:44 2019

@author: ROG-GL553VD
"""

#OOP Inheritance. Overriding, Private, Polymorphism

class Car:
    color = 'black'
    gear_position = 'N'
    __factory_number = '001234567' #private_attribute
    
    def __init__(self, transmission = 'manual'):
        self.transmission = transmission
        print(transmission+', Engine is ready!!')

    def drive(self):
        self.gear_position = 'D'
        print('Drive')

    def reverse(self):
        self.gear_position = 'R'
        print('Reverse. Please check your behind')
    
    def change_gear(self, gear='N'):
        self.gear_position = gear
        print('Gear position on: ' + self.gear_position)
    
    def get_gear_position(self):
        return self.gear_position
    
    def __get_factory_number(self): #private_method
        return self.__factory_number

class Tesla(Car): #Inheritance
    name = 'Etherium'

    def car_name(self, name = 'Etherium'): #Overriding
        self.name = name
        print('Hello friend, My name is '+ self.name)
    
    def change_gear(self):
        print('Sorry friend this automatic car')
        super().drive()

class NewCar(Tesla):
    pass

honda = Car('automatic')
honda.change_gear('D-1')
print('Gear Position Now: '+honda.get_gear_position())
honda.drive()
print(honda._Car__get_factory_number())

print()
tesla = Tesla('automatic')
tesla.car_name()
tesla.drive()
tesla.change_gear()
print(tesla._Tesla__get_factory_number())