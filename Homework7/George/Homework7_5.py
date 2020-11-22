# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:32:21 2020

@author: G

Title: Calculate run time
"""
# km/h
speed = float(input("Please input speed(km/h):"))
# meter
dist = 400

time = dist / (speed * (1000 / 3600))

if (time < 10):
    print("Invalid.")
else:
    print("Spend time: {:.2f} sec".format(time))
    
