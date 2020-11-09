# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:44:38 2020

@author: Fenrir

Description :
    1. 2で割り切れる場合「Multiple of 2」
    2. 3で割り切れる場合「Multiple of 3」
    3. 2と3同時に割り切れる場合「Multiple of 2 and 3」
    4. どちらも割り切れない場合「Not multiple of 2 and 3」

Variable:
    input: x
Algorithm/Calculation:
    x%2==0 and x%3==0 -> Multiple of 2 and 3  
"""
# if else
x = int(input("Input a number: "))
# ユーザーに入力させます
if x % 2 == 0 and x % 3 == 0:
# 「2 と 3同時」に割り切れる場合「Multiple of 2 and 3」    
    print(x,"is a multiple of 2 and 3.")
else:
    if x % 2 == 0:
        print(x,"is a multiple of 2.")
    else:
        if x % 3 == 0:
            print(x,"is a multiple of 3.")
        else:
           print(x,"is not a multiple of 2 or 3.") 
"""
# elif
x = int(input("Input a number: "))
# ユーザーに入力させます
if x % 2 == 0 and x % 3 == 0:
# 「2 と 3同時」に割り切れる場合「Multiple of 2 and 3」    
    print(x,"is a multiple of 2 and 3.")
elif x % 2 == 0:
# 2で割り切れる場合だけ
    print(x,"is a multiple of 2.")
elif x % 3 == 0:
# 3で割り切れる場合だけ    
    print(x,"is a multiple of 3.")
else:
# どちらも割り切れない場合
    print(x,"is not a multiple of 2 or 3.")
"""