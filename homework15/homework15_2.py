# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 18:16:04 2021

@author: Fenrir

Description :


"""






      
"""
def Leet_fun(c):
    list_char = ['A', 'E', 'G', 'I', 'O', 'S', 'Z']
    list_number = [4, 3, 6, 1, 0, 5, 2]
    if c in list_char:
        return str(list_number[list_char.index(c)])
    else: 
        return c
input_line = input()

ans_str = ''.join(list(map(Leet_fun, input_line))) 

print(ans_str)

"""