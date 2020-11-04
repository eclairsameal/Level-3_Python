# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 14:31:02 2020

@author: Fenrir

Description :
    奇数(odd)・偶数(even)を判定する(三項演算子)
    
Variable:
    Input: number
Algorithm/Calculation:
    number % 2 == 0 - > even
"""

number = int(input('Enter a number: '))
'''
if number % 2 == 0:
    print(number,'-> even')
else:
    print(number,'-> odd')
'''
# 三項演算子
print(number,'-> even') if number % 2 == 0 else print(number,'-> odd')