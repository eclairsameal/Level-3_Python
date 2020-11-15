# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:04:40 2020

@author: Fenrir

Description :

Variable:
    
Algorithm/Calculation:
"""

a = int(input("Input a:"))
b = int(input("Input b:"))
c = int(input("Input c:"))
if a + b > c and a + c > b and b + c > a:
    print(a + b + c)
else:
    print('Invalid')