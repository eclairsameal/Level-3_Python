# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 15:45:32 2020

@author: George

Title: Homework9-2
"""
import math

while(True):
    number = float(input("Please input number:"))
    if(number <= 0):
        print("Can't input under 0.")
    else:
        break
    
print(math.ceil(number)**2)

