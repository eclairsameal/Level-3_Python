# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:33:47 2020

@author: George

Title: Homework10_1

Explanation: 

"""

number = int(input("Please input number:"))

for i in range(number+1):
    if(i % 3 != 0):
        print(i, end = " ")
        
