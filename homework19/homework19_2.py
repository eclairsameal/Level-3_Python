# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:42:22 2021

@author: Fenrir

Description :
"""

# function
def row_99(n):
    for i in range(1, 10):
        print("{}*{}={:>2}".format(i, n, i*n), end = " ")
    print()
    
def all_99():
    for i in range(1, 10):
        row_99(i)
    print()
    
# main 
while True:
    print("1.九九を 1 行だけ表示する 2.九九表 3.End")
    select = int(input("Please select function(機能を選択してください): "))

    if select == 1:
        n = int(input("生成する数の九九を入力してください: "))
        row_99(n)
    elif select == 2:
        all_99()
    elif select == 3: 
        print("End")
        break
    else:  # 1〜4以外で入力する場合
        print("No option")