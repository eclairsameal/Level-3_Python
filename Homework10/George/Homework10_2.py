# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:42:02 2020

@author: George

Title: Homework10_2

Explanation: 

"""

num1 = int(input("Please input number1:"))
num2 = int(input("Please input number2:"))

count = 0

for i in range(1, 1001):
    if((i % num1 == 0) and (i % num2 == 0)):
        print(i, end = " ")
        count += 1

if(count == 0):
    print("---")