# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 15:30:24 2021

@author: Fenrir

Description :

"""
  
# -------------------- not function --------------------
n = int(input())
for i in range(n):
    str_list = input().split(' ')
    num_list = []
    for x in str_list:
        num_list.append(eval(x)) # string -> number
    print("{:.2f}".format(max(num_list) - min(num_list)))


# -------------------- function --------------------
def function():
    str_list = input().split(' ')
    num_list = []
    for x in str_list:
        num_list.append(eval(x)) # string -> number
    return max(num_list) - min(num_list) 

n = int(input())
for i in range(n):
    print("{:.2f}".format(function()))
    
    
 # -------------------- function_2 --------------------
def function(s): # 文字列を数値のリストに処理します
    str_list = s.split(' ')
    num_list = []
    for x in str_list:
        num_list.append(eval(x)) # string -> number
    return num_list

n = int(input())
for i in range(n):
    num_list = function(input())
    print("{:.2f}".format(max(num_list) - min(num_list)))   
    