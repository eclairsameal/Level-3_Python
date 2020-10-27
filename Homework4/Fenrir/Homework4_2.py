# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:14:06 2020

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
# input
a = input()
b = input()
c = input()
d = input()

#右詰め
print("|{:>10} {:>10}|".format(a, b))
print("|{:>10} {:>10}|".format(c, d))
#左詰め
print("|{:<10} {:<10}|".format(a, b))
print("|{:<10} {:<10}|".format(c, d))