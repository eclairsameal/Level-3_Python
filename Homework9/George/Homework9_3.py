# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 16:00:19 2020

@author: George

Title: Homework9-3
"""
number = int(input("Please input number:"))
temp = 2

while(temp < number):
    if(number%temp == 0):
        print("The number {} is not a prime number.".format(number))
        number = int(input("Please input number again:"))
        temp = 2
        continue
    temp += 1
print("The number {} is a prime number.".format(number))

