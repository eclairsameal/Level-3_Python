# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:24:33 2020

@author: Fenrir

Description :
    1.ユーザーに数値を一つ入力させ、入力された数値が0以下であれば再度入力させるようにする
    2.入力した数値を整数にし変数入れた後、その変数の値を自乗した結果を出力し、表示させること
"""
import math

number = -1
while number <= 0:
    number = float(input("Please input number:"))
    if(number <= 0):
        print("Can't input under 0.")
    else:
        print(math.ceil(number)**2)
        break