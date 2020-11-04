# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:54:40 2020

@author: Fenrir

Description :
    ユーザーに自然数を1つ入力させ、その数値に対し3か5の倍数であるかを判断させる。
Variable:
    Input: n
Algorithm/Calculation:
    n%5==0 and n%3==0
"""

x = int(input("Input number:"))

if x % 3 == 0 and x % 5 == 0:
    print(x,"is a multiple of 3 and 5.")
else:
    print(x,"is not a multiple of 3 or 5.")