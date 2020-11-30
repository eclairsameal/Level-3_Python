# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 16:12:52 2020

@author: George

Title: Homework9-4
"""
total = 0
prise = 0

while(True):
    number = int(input("Please input item number:"))
    if(number == 1):
        prise = 500
    elif(number == 2):
        prise = 800
    elif(number == 3):
        prise = 1600
    elif(number == 4):
        prise = 2200
    else:
        break
    
    total += prise
    print("Item prise is {}.".format(prise))
    print("Now total: {} yen".format(total))
    
print("You have to pay: {} yen".format(total))

