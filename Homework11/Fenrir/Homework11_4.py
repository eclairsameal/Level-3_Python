# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:49:04 2020

@author: Fenrir

Description :
            Please input number: 5
            Result:
            1
            1 3
            1 3 6
            1 3 6 10
            1 3 6 10 15
Variable:
   input: n 
"""
n = int(input("Please input number: "))
print("Result:")
for i in range(1, n+1):
    for j in range(1, i+1):
        print(sum(range(1, j+1)), end = " ")
    print()