# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:37:11 2020

@author: Fenrir

Description :
ユーザーに金額（例：10,000）、年間利回り（例5.75）、そして経過月数（例5）を入力させ、毎月の預金総額を計算する事。

四捨五入し、小数点以下2桁まで表示させること。

例えば、 預金額を$10,000とし、年間利回りが5.75％だとする。

1ヶ月目の預金総額は：　10000 + 10000 * 5.75 / 1200 = 10047.92
2か月目の預金総額は：　10047.92 + 10047.92 * 5.75 / 1200 = 10096.06
3か月目の預金総額は：　10096.06 + 10096.06 * 5.75 / 1200 = 10144.44
Variable:
    input: money gain month
"""

money = int(input("Please input money: "))
gain = float(input("Please input gain: "))
month = int(input("Please input month: "))

for i in range(month):
    money = money + money * (gain / 1200)
print("Your total money: {:.2f}".format(money))