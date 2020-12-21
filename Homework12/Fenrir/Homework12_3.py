# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 16:10:58 2020

@author: Fenrir

Description :
    乱数を8つ生成しそれをリストに格納し、そのリストに対し新たに数値を作成、挿入、削除等が可能になものを作ること。
"""
import random

list_number = []
for i in range(8): # 乱数を 8 つ生成
    list_number.append(random.randint(1, 100))
print(list_number)

while True:
    print("1.Add(追加) 2.Insert(挿入) 3.Delete(削除) 4.End")
    select = int(input("Please select function(機能を選択してください): "))

    if select == 1:
        n = int(input("New number（新しい数字）: "))
        list_number.append(n)
        # list_number.append(int(input("New number（新しい数字）: ")))
        print(list_number)
        
    elif select == 2:
        n = int(input("New number（新しい数字）:"))
        p = int(input("Insertion position (the first position is 1)[挿入位置（最初の位置は 1）]: "))
        list_number.insert(p - 1, n)
        # list_number.insert(int(input("Insertion position (the first position is 1)[挿入位置（最初の位置は1）]:")) - 1, int(input("New number（新しい数字）:")))
        print(list_number)
        
    elif select == 3:      
        n = int(input("Deleted number（削除された数字）:"))
        list_number.remove(n) 
        # list_number.remove(int(input("Deleted number（削除された数字）:")))
        print(list_number)
        
    elif select == 4: 
        print("End")
        break
    
    else:  # 1〜4以外で入力する場合
        print("No option")