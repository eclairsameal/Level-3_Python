# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:44:51 2020

@author: Fenrir

Description :
    
"""
import random
list_number = []
for i in range(8):
    n = random.randint(1, 100)
    list_number.append(n)
print(list_number)

input_number = int(input("Input :"))

flag = False
for i in range(8):
    if list_number[i] == input_number:
        flag = True
if flag:
    print("The number is in the list")
else:
    print("Number is not in the list")