# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 14:24:33 2020

@author: Fenrir

Description :
    Determine whether the input score is within a reasonable range(0~100)
Variable:
    Input: score
Algorithm/Calculation:
    score < 0 or score >100
"""
score = int(input("Input scorer:"))

if score < 0 or score >100 :
    print('Enter a number from 0 to 100 in score.')
else:
    print('score = {}'.format(score))