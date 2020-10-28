# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:25:26 2020

@author: Fenrir

Description :
    入力された成績を各々A(100 ~ 90)、B(89 ~ 80)、C(79 ~ 70)、D(69 ~ 60)、F(59 ~ 0)へのランク分けを行う。
Variable:
    score
Algorithm/Calculation:
    A(100 ~ 90)
    B(89 ~ 80)
    C(79 ~ 70)
    D(69 ~ 60)
    F(59 ~ 0)
"""
score = int(input("score: "))
if score >= 90:
    print('Grade is: A')
elif score >= 80:
    print('Grade is: B')
elif score >= 70:
    print('Grade is: C')
elif score >= 60:
    print('Grade is: D')
else:
    print('Grade is: F')