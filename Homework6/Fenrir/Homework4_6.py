# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 18:09:58 2020

@author: Fenrir

Description :
    1. 成績A、成績B、成績Cを入力出来るようにする
    2. これらの平均が合格点かどうか判断し合格であればそのまま平均点と合格を次の様に表示「XX point :Pass」
    3. もし不合格の場合、前述の方法にて「成績A」のみを再計算して再度平均点を算出し、合格か不合格を次の様に表示「XX point :Failure」
        補足：尚XXのポイントの小数点は切り上げて表示させること
Variable:
    Input: 
        - Aは授業態度成績(A is class attitude grade)
        - Bは抜き打ちテストの平均成績(B is the average test score)
        - Cは期末試験の成績(C is the final exam)
Algorithm/Calculation:
 - 新たな成績A = (math.sqrt(旧成績A))*10    
"""
import math

a = int(input("class attitude grade:"))
b = int(input("average test score:"))
c = int(input("final exam:"))
# original -> 15000
avg = ((a + b + c) / 3)
# Calculate average
if avg >= 60:
    print("{} point :Pass".format(math.ceil(avg)))
    # ポイントの小数点は切り上げ -> math.ceil()
else:
    a = math.sqrt(a) * 10
    # 新たな成績A = (math.sqrt(旧成績A))*10
    avg = ((a + b + c) / 3)
    if avg >= 60:
        print("{} point :Pass".format(math.ceil(avg)))
    else:
        print("{} point :Failure".format(math.ceil(avg)))