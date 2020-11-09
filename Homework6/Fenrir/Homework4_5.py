# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:55:45 2020

@author: Fenrir

Description :
    15000円を持って行ったとしましょう。
    1. 小計（円）を入力出来るようにすること（＜15000）
    2. 表を参考にして判断させ、支払いが済んだ後キャッシュバックされたお金も即時持って帰り所持金に加算する
    3. 買い物が済んだ時の残金を次のように表示させること「xxxxx yen」（xxxxx　は所持金額）
Variable:
    
Algorithm/Calculation:
    3000 ~ 5999 -> my_money - total_pay + 300 
    6000 ~ 9999 -> my_money - total_pay + 800
    10000 ~     -> my_money - total_pay + 1500
"""

my_money = 15000
# original -> 15000
total_pay = int(input("Please input pay:"))
# ユーザーに入力させます 
if total_pay >= 10000:
    my_money = my_money - total_pay + 1500
elif total_pay >= 6000:
    my_money = my_money - total_pay + 800
else:
    my_money = my_money - total_pay + 300
print("{} yen".format(my_money))