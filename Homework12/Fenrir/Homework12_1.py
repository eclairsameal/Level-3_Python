# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 21:05:29 2020

@author: Fenrir

Description : 
    ユーザーに入力させ「-1」が入力されるまで、その後にユーザーが入力した数字と入力した回数を出力表示すること。

"""
list_number = []
while True:
    n = int(input("input: "))
    if n == -1:
        break
    list_number.append(n)
print("List:", list_number)
print("len:", len(list_number))