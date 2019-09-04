# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 15:56:44 2019

@author: ROG-GL553VD
"""

#OOP

class Car:
    color = 'black'
    gear_position = 'N'
    
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
    
honda = Car('automatic')
honda.change_gear('D-1')
print('Gear Position Now: '+honda.get_gear_position())
honda.drive

print()
toyota = Car()
print('Gear Position Now: '+toyota.get_gear_position())
toyota.drive()