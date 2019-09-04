# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 17:16:32 2019

@author: ROG-GL553VD
"""

#Example OOP
class Employee:
    'Abstract base class Employee'
    
    def __init__(self, first, last):
        """Employee contructor, take first name and lat name.
        NOTE: cannot create object of class Employee."""
        
        if self.__class__ == Employee:
            raise NotImplementedError 
                        "Cannot create object of class Employee"
        
        self.firstName = first
        self.lastName = last
    
    def __str__ (self):
        """Strinf representation of Employee"""
        
        return "%s %s" % (self.firstName, self.lastName)
    
    def _checkPositive(self, value):
        """Utility method to ensure a value is positive"""
        
        if value < 0:
            raise ValueError("Attribute value (%s) must be positive" % value)
        else:
            return value
    
    def earnings (self):
        """Abstract method; deriver classes must override"""
        raise NotImplementedError("Cannot call abstract method")
    
class Boss (Employee):
    """Boss class, inherits from Employee"""
    
    def __init__ ( self, first, last, salary ):
        """Boss constructor, take first, last name and salary"""
        Employee.__init__(self, first, last)
        self.weeklySalary = self._checkPositive(float(salary))
        
    def earnings (self):
        """Compute the Boss's pay"""
        return self.weeklySalary
    
    def __str__(self):
        """string representation of boss"""
        return "%17s: %s" % ("Boss",Employee.__str__(self))
    
class CommissionWorker (Employee):
    """CommissionWorker class, inherits from Employee"""
    
    def __init__(self, first, last, salary, commission, quantity):
        """CommissionWorker constructor, takes first and last names, salary, commission adn quantity"""
        
        Employee.__init__(self, first, last)
        self.salary = self._checkPositive(float(salary))
        self.commission = self._checkPositive(float(commission))
        self.quantity = self._checkPositive(quantity)
        
    def earnings (self):
        """Compute the CommissionWorker pays"""
        return self.salary + self.commission * self.quantity
    
    def __str__ (self):
        """String representation of CommissionWorker"""
        
        return "%17s: %s" % ( "Commission Worker", Employee.__str__(self))

class PieceWorker (Employee):
    """PieceWorker class, inherits from Employee"""
    
    def __init__(self, first, last, wage, quantity):
        """PieceWorker constructor, takes first and last names, salary, commission adn quantity"""
        
        Employee.__init__(self, first, last)
        self.wagePerPiece = self._checkPositive(float(wage))
        self.quantity = self._checkPositive(quantity)
        
    def earnings (self):
        """Compute the PieceWorker pays"""
        return self.quantity * self.wagePerPiece
    
    def __str__ (self):
        """String representation of PieceWorker"""
        
        return "%17s: %s" % ( "Piece Worker", Employee.__str__(self))

class HourlyWorker (Employee):
    """HourlyWorker class, inherits from Employee"""
    
    def __init__(self, first, last, wage, hours):
        """HourlyWorker constructor, takes first and last names, salary, commission adn quantity"""
        
        Employee.__init__(self, first, last)
        self.wagePerPiece = self._checkPositive(float(wage))
        self.hours = self._checkPositive(hours)
        
    def earnings (self):
        """Compute the HourlyWorker pays"""
        if self.hours <= 40:
            return self.wagePerPiece * self.hours
        else:
            return 40 * self.wagePerPiece * (self.hours-40) * self.wagePerPiece * 1.5
    
    def __str__ (self):
        """String representation of HourlyWorker"""
        
        return "%17s: %s" % ( "Hourly Worker", Employee.__str__(self))

employees = [
            Boss ("John", "Smith", 800.00),
            CommissionWorker("Sue", "Jones", 200.00, 3.0, 150),
            PieceWorker("Bob", "Lewis", 2.5, 200),
            HourlyWorker("Karen", "Price", 13.75, 40)
        ]

for employee in employees:
    print ("%s earned $%.2f" % (employee, employee.earnings()))
