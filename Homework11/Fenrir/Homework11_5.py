# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:49:04 2020

@author: Fenrir

Description :
      入力が「7」の場合

      *
     **
    ***
   ****
  *****
 ******
*******
Variable:
   input: n 
"""
n = int(input("Please input number: "))

# for 
for i in range(1, n+1):
    for j in range(n-i, 0, -1):
        print(" ", end = "")
    for j in range(1, i+1):
        print("*", end = "")
    print()
     
"""  
# string * n
print("Result:")
for i in range(1, n+1):
    print(" "*(n-i), end="")
    print("*"*i)
"""