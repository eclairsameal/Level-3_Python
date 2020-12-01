# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:54:19 2020

@author: George

Title: Homework10_4

Explanation: 

"""

num = int(input("Please input the number between 1 to 9:"))

for i in range(1, 10):
    print("{}x{} = {:>2}".format(num, i, num * i))