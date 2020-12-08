# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:12:08 2020

@author: Fenrir

Description :
    ユーザーに2つの数値（自然数）を入力させる
    入力された数値の間（その数値も含み）に含まれる全ての偶数を加算後、その結果を出力し表示させること
Variable:
    input: num1, num2 
"""
num1 = int(input("Please input number1:"))
num2 = int(input("Please input number2:"))

total = 0
for i in range(num1, num2+1):
    if i % 2 == 0:
        total +=i 
print(f"Total = {total}")    