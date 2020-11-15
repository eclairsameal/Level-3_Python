# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 16:20:54 2020

@author: Fenrir

Description :
    Winter(1 ~ 3)
    Spring(4 ~ 6)
    Summer(7 ~ 9)
    Autumn(10 ~ 12)
    範囲外の数値が入力された場合、「○○ not in range.」と表示する(○○は入力された数値)
Variable:
    月数 : month
Algorithm/Calculation:
    
"""
# if else
month = int(input("Please input month: "))
# 月は数字なので、数字に変換する必要があります
if month < 1 or month > 12:
    print("{} not in range.".format(month))
else:
    if month < 4:
        print("Winter")
    else:
        if month < 7:
            print("Spring")
        else:
            if month < 10:
                print("Summer")
            else:
                print("Autumn")

"""
# elif
month = int(input("Enter the month: "))
# 月は数字なので、数字に変換する必要があります
if month < 1 or month > 12:
    print("{} not in range.".format(month))
elif month < 4:
    print("Winter")
elif month < 7:
    print("Spring")
elif month < 10:
    print("Summer")
else:
    print("Autumn")
"""