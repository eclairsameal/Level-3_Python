# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 16:08:05 2020
@author: George
"""

a = float(input("Please input a:"))
b = float(input("Please input b:"))
c = float(input("Please input c:"))

s = ( a + b + c ) / 2

areaS = ( s * ( s - a ) * ( s - b ) * ( s - c )) ** 0.5

print("The S(Area) is",  areaS)
print("The s is",  s)

