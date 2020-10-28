# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 18:23:19 2020

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
else:
    if score >= 80:
          print('Grade is: B')
    else:
      if score >= 70:
        print('Grade is: C')
      else:
          if score >= 60:
            print('Grade is: D')
          else:   
            print('Grade is: F')