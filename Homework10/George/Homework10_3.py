# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:50:34 2020

@author: George

Title: Homework10_3

Explanation:  

"""

num1 = int(input("Please input number1:"))
num2 = int(input("Please input number2:"))

total = 0

for i in range(num1, num2 + 1):
    if(i % 2 == 0):
        total += i
        
print("Total = {}".format(total))