# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 14:42:22 2021

@author: Fenrir

Description :
"""

def compute(a, b): # * ユークリッドの互除法
    m = a % b
    while (m > 0):
        a = b
        b = m
        m = a % b
    return b

def compute_1(a, b): 
    # 範囲として最小値を取ります
    '''
    if a < b:  
        min_val = a
    else:
        min_val = b
    '''
    min_val = (a, b)
    gcd_val = 1    
    for i in range(1, min_val + 1):
        if a % i == 0 and b % i == 0: # a と b の両方が割り切れる場合
            gcd_val = i        
    return gcd_val

def compute_2(a, b): 
    min_val = (a, b) # 範囲として最小値を取ります
    for i in range(min_val, 3, -1):
        if a % i == 0 and b % i == 0: # a と b の両方が割り切れる場合
            gcd_val = i  
            break
    return gcd_val

x = int(input("input x: "))
y = int(input("input y: "))
m = int(input("input m: "))
n = int(input("input n: "))

p = x * n + y * m
q = y * n

print("{}/{} + {}/{} = {}/{}".format(x, y, m, n, int(p/compute(p, q)), int(q/compute(p, q))))
print("{}/{} + {}/{} = {}/{}".format(x, y, m, n, int(p/compute_1(p, q)), int(q/compute_1(p, q))))
print("{}/{} + {}/{} = {}/{}".format(x, y, m, n, int(p/compute_2(p, q)), int(q/compute_2(p, q))))
