# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:38:30 2021

@author: Fenrir

Description :
    
"""

import random

def print_list(funlist): # output list function
    print("List: ",  end = "")
    for x in funlist:
        print(x, end = " ")
    print()
        
def random_list(n):    # 乱数を n つ生成
    funlist = []
    for i in range(n): # 乱数を n つ生成
        funlist.append(random.randint(1, 10))
    return funlist

def add_n_val(funlist, n):  # n個の値を追加します
    for i in range(n):
       funlist.append(int(input("New number（新しい数字）: ")))
    return funlist

def insert_n_val(funlist, n, p):  # n個の値を挿入します
    for i in range(n):
       funlist.insert(p - 1 + i, int(input("New number（新しい数字）: ")))
    return funlist

def remore_all_val(funlist, n): # すべての n を削除します
    # print(funlist)
    while n in funlist:
        funlist.remove(n)
    return funlist
    
list_number = random_list(5)
print_list(list_number)

while True:
    print("1.Add(追加) 2.Insert(挿入) 3.Delete(削除) 4.End")
    select = int(input("Please select function(機能を選択してください): "))

    if select == 1:
        n = int(input("Please enter how many to add（ ）: "))
        list_number = add_n_val(list_number, n)
        print_list(list_number)
        
    elif select == 2:
        n = int(input("Please enter how many to insert（ ）: "))
        position  = int(input("Insertion position (the first position is 1)[挿入位置（最初の位置は 1）]: "))
        list_number = insert_n_val(list_number, n, position)
        print_list(list_number)
        
    elif select == 3:      
        n = int(input("Deleted number（削除された数字）:"))
        list_number = remore_all_val(list_number, n) 
        print_list(list_number)
        
    elif select == 4: 
        print("End")
        break
    
    else:  # 1〜4以外で入力する場合
        print("No option")