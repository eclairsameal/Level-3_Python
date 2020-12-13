# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:58:25 2020

@author: Fenrir

Description :
    ユーザーに2つの数値（自然数）を入力させる
    数字の１～１０００までの間で、入力された数値の公倍数だけを出力し表示させること
    一つも表示されないときは、「—」と表示させること
Variable:
    input: num1, num2
"""
num1 = int(input("Please input number1:"))
num2 = int(input("Please input number2:"))

n = num1*num2 
if n > 1000:
    print("---")
else:
    for i in range(1, 1001):
        if((i % num1 == 0) and (i % num2 == 0)):
            print(i, end = " ")
