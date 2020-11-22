# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 16:08:05 2020
@author: George

Title: BMI Calculate
"""

height = float(input("Please input your height(cm):"))
weight = float(input("Please input your weight(kg):"))

bmi = weight / ((height / 100) ** 2)
comment = ""

if (bmi < 18.5):
    comment = "Underweight"
elif (bmi < 25):
    comment = "Normal weight"
elif (bmi < 30):
    comment = "Overweight"
else:
     comment = "Obese"       

print("Your BMI is {:.2f}:".format(bmi))
print("comment:{}".format(comment))


