# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 14:56:41 2020

@author: Fenrir

Description :
    ユーザーに数字（西暦）を入力させ、
    閏年「leap year」であるかを判断することが出来るプログラムを作成してください。
    1. 数字が4の倍数であればその年は閏年「leap year」と表示
    2. 但し数字が100の倍数であれば2.よりも優先されその年は平年「Normal year」と表示
    3. 更に数字が400の倍数であれば3.よりも優先されその年は閏年「leap year」と表示
Variable:
    year  
Algorithm/Calculation:
"""

y = int(input('Please input year:'))
print("{} is a leap year.".format(y)) if y % 4 ==0 and y % 100 != 0 or y % 400 == 0 else print("{} is a normal year.".format(y))

"""
y = int(input('Please input year:'))
if y % 4 ==0 and y % 100 != 0 or y % 400 == 0:
    print("{} is a leap year.".format(y))
else :
    print("{} is a normal year.".format(y))
"""

"""   
# version: nest if
year = int(input('Please input year:'))

if(year % 400 == 0):
    print('{} is a leap year.'.format(year))
else:    
    if(year % 100 == 0):
        print('{} is a normal year.'.format(year))
    else:
        if(year % 4 == 0):
            print('{} is a leap year.'.format(year))
        else:
            print('{} is a normal year.'.format(year))
"""
"""   
# version: elif
if( year % 400 == 0):
    print('{} is a leap year.'.format(year))
elif( year % 100 == 0):
    print('{} is a normal year.'.format(year))
elif( year % 4 == 0):
    print('{} is a leap year.'.format(year))
else:
    print('{} is a normal year.'.format(year))
"""