# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:47:08 2020

@author: Fenrir

Description :
    成績を入力し、それを出力する。
    もし成績が60に満たなければ"Fail grades"と出力する。
Variable:
    成績: grades
"""

grades = int(input("Input Grades: "))
# Conditions
if(grades < 60):
    print("Fail grades")    
print("Grades:", grades)