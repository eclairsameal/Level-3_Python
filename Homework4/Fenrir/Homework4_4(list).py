# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:33:30 2020

@author: Fenrir

Description :
    数値の表示、総計、及び平均数値を表示する事。
    総計値と平均値、全て小数点以下は1桁に留める事。
Variable:
    Input: num[]

Algorithm/Calculation:
    sum = sum(num)
    average = sum(num)/len(num)
"""

num = []
for i in range(5):
    x = eval(input())
    num.append(x)
print(num[0], num[1], num[2], num[3], num[4])
print("Sum = {:.1f}".format(sum(num)))
print("Average = {:.1f}".format(sum(num)/len(num)))