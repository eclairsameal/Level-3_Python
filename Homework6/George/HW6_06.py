# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:21:58 2020

@author: G
"""
import math

examA = int(input("Please input examA: "))
examB = int(input("Please input examB: "))
examC = int(input("Please input examC: "))

total = examA + examB + examC
avg = total / 3

if (avg < 60):
    examA = math.sqrt(examA) * 10
    
    total = examA + examB + examC
    avg = total / 3
    if(avg < 60):
        print("{:2} point: Failure".format(math.ceil(avg)))
    else:
        print("{:2} point: Pass".format(math.ceil(avg)))
else:
    print("{:2} point: Pass".format(math.ceil(avg)))
    

