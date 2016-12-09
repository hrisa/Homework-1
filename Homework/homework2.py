# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 17:13:11 2016

@author: Hristina
"""

from numpy import linspace
from matplotlib import pyplot as plt

class Interval:
    
############################### TASK 1/7 ###############################
    
    def __init__(self, a, b = None):
        if not a <= b:
            raise TypeError('The first number should be smaller than the second one.')
        self.a = a
        if(b == None): self.b = self.a
        if(b != None): self.b = b
        
############################### TASK 2/6/8 ###############################

    def __add__(self, second):
        if not isinstance(second, Interval):
            return Interval(self.a + second, self.b + second)
        return Interval(self.a + second.a, self.b + second.b)
        
    def __radd__(self, second):
        return Interval(self.a + second, self.b + second)

    def __sub__(self, second):
        if not isinstance(second, Interval):
            return Interval(self.a - second, self.b - second)
        return Interval(self.a - second.b, self.b - second.a)
        
    def __rsub__(self, second):
        return Interval(second - self.b, second - self.a)
    
    def __mul__(self, second):
        if not isinstance(second, Interval):
            return Interval(min(self.a*second, self.b*second),
                            max(self.a*second, self.b*second))
        a2, b2 = second.a, second.b
        return Interval(min(self.a*a2, self.a*b2, self.b*a2,
                            self.b*b2), max(self.a*a2, self.a*b2, 
                            self.b*a2, self.b*b2))
        
    def __rmul__(self, second):
        return Interval(min(self.a*second, self.b*second),
                            max(self.a*second, self.b*second))
        
    def __truediv__(self, second):
        if not isinstance(second, Interval):
            raise TypeError('The argument should be of type Interval.')
        if second.a == 0:
            raise TypeError('The arguments of the second interval should be different from zero.')
        if second.b == 0:
            raise TypeError('The arguments of the second interval should be different from zero.')
        a2, b2 = second.a, second.b
        return Interval(min(self.a/a2, self.a/b2, self.b/a2, self.b/b2), 
                        max(self.a/a2, self.a/b2, self.b/a2, self.b/b2))

############################### TASK 3 ###############################
        
    def __repr__(self):
        return '[' + str(self.a) + ', ' + str(self.b) + ']'
        
############################### TASK 5 ###############################

    def __contains__(self, value):
        return self.a <= value and self.b >= value
                
############################### TASK 9 ###############################

    def __pow__(self,n):
        if n < 0:
            raise TypeError('Please, enter a positive number.')
        if n % 2 != 0:
            return Interval(self.a**n, self.b**n)
        if n % 2 == 0:
            if self.a >= 0:
                return Interval(self.a**n, self.b**n)
            elif self.b < 0:
                return Interval(self.b**n, self.a**n)
            return Interval(0.0, max(self.a**n, self.b**n)) 

############################### TASK 4 ###############################
                 
#I1 = Interval(1.0, 4.0)
#I2 = Interval(-2.0, -1.0)
#print(I1 + I2)
#print(I1 - I2)
#print(I1 * I2)
#print(I1 / I2)

#print(I1.__contains__(0.5))
#print(I1.__contains__(3.5))
#print(I1.__contains__(5.5))

#print(Interval(2, 3) + 1)
#print(1 + Interval(2, 3))
#print(1.0 + Interval(2, 3))
#print(Interval(2, 3) + 1.0)
#print(1 - Interval(2, 3))
#print(Interval(2, 3) - 1)
#print(1.0 - Interval(2, 3))
#print(Interval(2, 3) - 1.0)
#print(Interval(2, 3) * 1)
#print(1 * Interval(2, 3))
#print(1.0 * Interval(2, 3))
#print(Interval(2, 3) * 1.0)

#x = Interval(-2., 2.)
#print(x**2)
#print(x**3)

############################### TASK 10 ###############################

xl = linspace(0., 1, 10)
xu = linspace(0., 1, 10) + 0.5
intervals = [Interval(xl[i], xu[i]) for i in range(len(xl))]
poly = [3*(i**3) - 2*(i**2) - 5*i - 1 for i in intervals]
yl = [poly[i].a for i in range(len(poly))]
yu = [poly[i].b for i in range(len(poly))]

plt.plot(xl, yl)
plt.plot(xl, yu)
plt.xlabel('x')
plt.ylabel('p(I)')
plt.title('$p(I)=3I^3 - 2I^2 - 5I - 1$, I = Interval(x,x+0.5)')