# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:51:39 2020

@author: G
"""

pay = int(input("Please input pay:"))
cashBack = 0
money = 15000
if (pay >= 10000):
    cashBack = 1500
elif (pay >= 6000):
    cashBack = 800
elif (pay >= 3000):
    cashBack = 300

money = money - pay + cashBack

print("money: {}".format(money))

