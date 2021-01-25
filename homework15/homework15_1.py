# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:52:18 2021

@author: Fenrir

Description :
連続で入力できるようにする
数値以外の物が入力された場合、それをリストには入れず再度入力させる（例えば、「abcde」と入力されたらリストには入れず再度入力を続行できるようにすること）
「-9999」が入力されたら入力を終了し、全てを出力する（-9999はリストに含めず）
最大値、最小値、合計値、平均値を出力する

"""
list_a = []

while True:
    n = input("Input :")
    if n == "-9999":
        break
    while not n.isdigit():
        print("not number")
        n = input("Input :")

    list_a.append(int(n))
  
print("最大値:{}".format(max(list_a)))
print("最小値:{}".format(min(list_a)))
print("合計値:{}".format(sum(list_a)))
print("平均値:{}".format(sum(list_a)/len(list_a)))
