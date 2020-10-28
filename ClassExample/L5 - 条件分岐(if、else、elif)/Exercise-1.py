# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:26:58 2020

@author: Fenrir

Description :
    1. 数字を1つ入力することが出来る
    2. 入力した数字が奇数であれば「Odd number」と出力する
    3. 入力した数字が偶数であれば「Even number」と出力する
Variable:
    x
Algorithm/Calculation:
    x % 2 ==0 - > Even(偶数)
"""
x = int(input())
if x % 2 ==0 :
    print("{} is an Even number.".format(x))
else :
    print("{} is an Odd number.".format(x))