# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 16:24:44 2020

@author: George

Title: Homework9-5
"""
customerA = 0
customerB = 0
customerC = 0
total = 0

while(True):
    age = int(input("Please input the customer's age:"))
    if(age < 0):
        break
    elif(age < 18):
        customerA += 1
    elif(age < 40):
        customerB += 1
    else:
        customerC += 1
        
    total += 1
    
print("Today's cutomers info:")
print("Age 0 to 17:", customerA)
print("Age 18 to 40:", customerB)
print("Age 40 or more:", customerC)
print("Total customers:", total)
