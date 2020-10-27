# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:15:17 2020

@author: Fenrir

Description :
    円周、円面積を計算することが出来るプログラムを作る。
    入力するのは「半径」のみ、「π」は3.14で計算する。
    
Variable:
    input：半径(r)
    output：円周(circumference)
    output：円面積(area)
    
Algorithm/Calculation:
    circumference = r * 2 * 3.14
    area = r * r * 3.14
"""
# input
r = float(input("Please input value r:")) # string to float

# Calculation
circumference = r * 2 * 3.14   # 円周
area = r * r * 3.14   # 円面積

# output
print("The circumference:", circumference)
print("The area:", area)