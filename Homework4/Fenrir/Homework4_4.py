# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:33:30 2020

@author: Fenrir

Description :
    数値の表示、総計、及び平均数値を表示する事。
    総計値と平均値、全て小数点以下は1桁に留める事。
Variable:
    Input:(a~e)
    sum:総計
    average:平均数
Algorithm/Calculation:
    sum = a + b + c + d + e
    average = sum/5
"""

# input
a = int(input("input a:"))
b = int(input("input b:"))
c = int(input("input c:"))
d = int(input("input d:"))
e = int(input("input e:"))

# Calculation
sum = a + b + c + d + e
average = sum/5

# output
print("Sum = {:.1f}".format(sum))
print("Average = {:.1f}".format(average))