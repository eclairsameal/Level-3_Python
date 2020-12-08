# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:21:39 2020

@author: Fenrir

Description :
    ユーザーに数値１～９の間で入力し段数を指定させること
    入力された数値に合わせて指定された段数の掛け算表を表示する事
Variable:
    input: n
"""
n = int(input("Please input the number between 1 to 9:"))
for i in range(1, 10):
    print(f"{n} x {i} = {n*i}")