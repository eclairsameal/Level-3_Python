# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:33:30 2020

@author: Fenrir

Description :
    正n角形の面積計算
    表示する際、小数点以下は4桁に留める事。
Variable:
    n: 正n角形
    s: Side length
    area: 面積
Algorithm/Calculation:
    Area = (n * pow(s, 2))/(4 * tan(pi/n))
"""
import math 
# input
n = float(input())
s = float(input())
# Calculation
area = (n * math.pow(s, 2))/(4 * math.tan(math.pi/n))
# output
print('Area = {:.4f}'.format(area))