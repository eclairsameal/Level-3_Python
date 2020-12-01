# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 18:02:29 2020

@author: George

Title: Homework10_5

Explanation:

"""

money = int(input("Please input money: "))
yearGain = float(input("Please input gain: "))
month = int(input("Please input month: "))

total = money

for i in range(month):
    total = total + total * (yearGain / 1200)
    
print("Your total money: {:.2f}".format(total))

