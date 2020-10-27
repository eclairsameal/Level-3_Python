# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:10:14 2020

@author: Fenrir

Description :
    Displaying integers in the specified format
Input:
    a, b, c, d
Output:
   |   a     b|
   |  c   d|
   |a    b    |
   |c   d  | 
"""
# input
a = []
for i in range(4):
    x = int(input())
    a.append(x)
#右詰め
print("|{:>5} {:>5}|".format(a[0], a[1]))
print("|{:>5} {:>5}|".format(a[2], a[3]))

#左詰め
print("|{:<5} {:<5}|".format(a[0], a[1]))
print("|{:<5} {:<5}|".format(a[2], a[3]))
