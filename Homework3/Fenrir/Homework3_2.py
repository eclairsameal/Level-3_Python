# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:35:30 2020

@author: Fenrir

Description :
    Triangle area
    
Variable:
    Side length: a, b, c
    Triangle area: S
    
Algorithm/Calculation:
    S = sqrt(s(s-a)(s-b)(s-c))
    s = a+b+c/2
"""
# input ide length (string to float)
a = float(input("Please input a:")) 
b = float(input("Please input b:")) 
c = float(input("Please input c:")) 

# Calculation
s = (a + b + c) / 2
S = (s  *(s - a) * (s - b) * (s - c)) ** (1 / 2)

"""
# Other answers   
import math
S = math.sqrt(s  *(s - a) * (s - b) * (s - c))
"""
# output
print("The S(Area) is ", S)
print("The s is ", s)
