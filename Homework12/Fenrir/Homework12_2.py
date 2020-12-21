# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:04:50 2020

@author: Fenrir

Description :
    37 82 53 18 87 10 61 58 23 51 
    AVERAGE = 48.00
    MAX = 87
    MIN = 10
"""
import random

'''
# not function
sum = 0
list_number = []
for i in range(10):
    n = random.randint(1, 101)
    sum+=n
    list_number.append(n)
    if i == 0:
        max_n = n
        min_n = n
    else:
        if n > max_n:
            max_n = n
        if n < min_n:
            min_n = n
    print(n, end = " ")
print()
print("AVERAGE = {}".format(sum/10))
print("MAX = {}".format(max_n))
print("MIN = {}".format(min_n))
'''
# list and function
list_number = []
for i in range(10):
    n = random.randint(1, 100)
    list_number.append(n)
    print(n, end = " ")
print()
print("AVERAGE = {:.2f}".format(sum(list_number)/10))
print("MAX = {}".format(max(list_number)))
print("MIN = {}".format(min(list_number)))



