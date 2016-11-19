# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 18:34:49 2016

@author: Calin Jilavu
"""

############################### TASK 1 ###############################
def f(x):
    return x**2


def ctrapezoidal(f, a, b, n):
    h = (b - a)/n
    Ih = h*(f(a)+f(b))/2
    for i in range(1,n):
        Ih += h * f(a + i*(b-a)/n)
    return Ih
    
############################### TASK 2 ###############################

tol = (float)(input("Gib tolerance pls: "))

init = ctrapezoidal(f,0,1,1)
I = ctrapezoidal(f,0,1,2)
i = 2

while(abs(I-init) >= tol):
    i+=1
    init = I
    I = ctrapezoidal(f,0,1,i)

print("Final result: {}".format(I))
