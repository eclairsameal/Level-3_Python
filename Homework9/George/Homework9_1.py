# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 15:27:59 2020

@author: George

Title: Homework9-1
"""
number = 1

while(number <= 100):
    if(number%3 == 0 and number%5 != 0):
        print(number, end = " ")
    number += 1
    
