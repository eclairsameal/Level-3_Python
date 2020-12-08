# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:49:04 2020

@author: Fenrir

Description :
    ユーザーに数値（自然数）を入力させる。
    数字の１から入力された数値までの間で３で割り切れない数値を全て出力し表示させること
Variable:
   input: n 
"""
n = int(input("Please input number:"))

for i in range(n+1):
    if i % 3 == 0:
        continue
    else:
        print(i, end = " ")