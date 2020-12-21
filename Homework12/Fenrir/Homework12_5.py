# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 18:13:33 2020

@author: Fenrir

Description :

Variable:
    
Algorithm/Calculation:
"""
import random
list_number = []
for i in range(8):
    n = random.randint(1, 99)
    list_number.append(n)
print(list_number)

for i in range(7): # 0 ~ 6
    for j in range(i, 8): # 1 ~ 7
        if list_number[j] < list_number[i]:  # list_number[j]とlist_number[i]交換
            temp = list_number[j]
            list_number[j] = list_number[i]
            list_number[i] = temp
print(list_number)