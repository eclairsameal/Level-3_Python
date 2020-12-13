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
import random

sum = 0

for i in range(10):
    n = random.randint(1, 101)
    sum+=n
    if i == 0:
        max_n = n
        min_n = n
    else:
        if n > max_n:
            max_n = n
        if n < min_n:
            min_n = n
    print(n, end = " ")
print()
print("AVERAGE = {}".format(sum/10))
print("MAX = {}".format(max_n))
print("MIN = {}".format(min_n))