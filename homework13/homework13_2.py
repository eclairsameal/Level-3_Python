# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 19:50:10 2021

@author: Fenrir

Description :

Variable:
    
Algorithm/Calculation:
"""

card_money = int(input("最初にチャージする現金: ")) # カード残額(最初にチャージする現金)
point = 0  # ポイント
n = int(input("乗車回数: ")) # 数回取る
for i in range(n):
    car_money = int(input()) # 運賃
    if point >= car_money: # 支払う運賃以上のポイントがある場合
        point-=car_money 
    else:
        card_money-= car_money
        point+=int(car_money/10) 
    print(f"カード残高:{card_money} ポイント:{point}")# 毎回の降車時に残っているお金とポイントを出力します。