# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:03:10 2021

@author: Fenrir

Description :

Variable:
    
Algorithm/Calculation:
"""
import random

def random_list(n, a, b): # list size, val = a ~ b
    list_a = []
    for i in range(n):
        random_var = random.randint(a, b) # 乱数はa〜bの値を生成します
        while random_var in list_a: # もし重複したら、もう一度乱数を生成します
            random_var = random.randint(a,b) 
        list_a.append(random_var) # リストに値を追加します
    print(list_a)

random_n = int(input("Please enter list size: "))
a = int(input("Please enter a: "))
b = int(input("Please enter b: "))
while b < a or (b - a) < random_n: # 制限が満たされていない場合
    print("Please enter again") # もう一度入力します。
    random_n = int(input("Please enter list size: "))
    a = int(input("Please enter a: "))
    b = int(input("Please enter b: "))

random_list(random_n, a, b) # 関数を呼び出す