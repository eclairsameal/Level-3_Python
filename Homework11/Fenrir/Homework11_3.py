# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:49:04 2020

@author: Fenrir

Description :
    ユーザーに自然数を1つ入力させ、その自然数の順番を反転させて出力する事。 
    並びに入力された数値が0かどうかを検出し、そうであれば0を出力する事。
Variable:
   input: n 
"""
# 方法1: math
n = int(input("Please input number: "))

while n != 0:
    print(n % 10, end="")
    n =int(n / 10)

'''
# 方法2: スライス(slice)
n=input()
print(n[::-1])
'''  
