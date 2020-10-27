# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 15:24:45 2020

@author: Fenrir

Description :
    「v1」「v2」のを入力できるようにする。
    平均速度「v」を計算できるようにする。
    
Variable:
    速度:v1, v2
    平均速度:v
    
Algorithm/Calculation:
    v = 2(v1 * v2) / (v1 + v2)
    
"""

# input (string to float)
v1 = float(input("Please input v1:")) 
v2 = float(input("Please input v2:")) 

# Calculation
v =( 2 * v1 * v2) / (v1 + v2)

# output
print("The average speed is", v)