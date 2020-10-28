# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:59:26 2020

@author: Fenrir

Description :
    Check whether the score is passing
Variable:
    score
Algorithm/Calculation:
    score >= 60 -> PASS
    score < 60 -> FAIL
"""
score = int(input('Enter a score: '))
# Conditions
if score >= 60:
    print(score,':PASS')
else:   # score < 60
    print(score,':FAIL')
