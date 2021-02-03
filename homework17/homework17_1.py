# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:38:30 2021

@author: Fenrir

Description :
    返り値は数値「a」～「b」の累加結果を返すことが出来る
"""

def sum_sb(a, b):
    sum_val = 0
    for x in range(a, b + 1):
        sum_val += x
    return sum_val

a = int(input("input a: "))
b = int(input("input b: "))
print("sum(a ~ b): ", sum_sb(a, b))
