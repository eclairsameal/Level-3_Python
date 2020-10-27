# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:03:04 2020

@author: Fenrir

Description :
    Displaying integers in the specified format
    スペース = 5
Input:
    a, b, c, d
Output:
   |   a     b|
   |  c   d|
   |a    b    |
   |c   d  | 
"""
# input
a = int(input())
b = int(input())
c = int(input())
d = int(input())
#右詰め
print("|{:>5} {:>5}|".format(a, b))
print("|{:>5} {:>5}|".format(c, d))
#左詰め
print("|{:<5} {:<5}|".format(a, b))
print("|{:<5} {:<5}|".format(c, d))
