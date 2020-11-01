# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:21:27 2020

@author: Fenrir

Description :
    矩形面積の計算(Calculation of rectangular area)
    表示する際は、高さ（Height）、幅（Width）、周りの長さ（Perimeter）、そして面積（Area）を表示する事。
    小数を表示する際、小数以下は2桁に留める事。
Variable:
    高さ: h
    幅: w
    周りの長さ: perimeter
    面積: area 
Algorithm/Calculation:
    perimeter = 2(h+w)
    area = hw
"""
# input
h = float(input("Input Height:"))
w = float(input("Input Width:"))
# output
print("Height = {:.2f}".format(h))
print("Width = {:.2f}".format(w))
print("Perimeter = {:.2f}".format((2 * (h + w))))
print("Area = {:.2f}".format(h * w))

'''
# Other answers 
perimeter = 2 * (h + w)
print("Perimeter = {:.2f}".format(perimeter))
area = h * w
print("Area = {:.2f}".format(area))
'''
