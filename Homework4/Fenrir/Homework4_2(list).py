# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:14:07 2020

@author: Fenrir

Description :
    Displaying integers in the specified format
    スペース = 10
Input:
    a, b, c, d
Output:
   |   a     b|
   |  c   d|
   |a    b    |
   |c   d  | 
"""
a = []
for i in range(4):
    x = str(input())
    a.append(x)
#右詰め
print("|{:>10} {:>10}|".format(a[0], a[1]))
print("|{:>10} {:>10}|".format(a[2], a[3]))

#左詰め
print("|{:<10} {:<10}|".format(a[0], a[1]))
print("|{:<10} {:<10}|".format(a[2], a[3]))
