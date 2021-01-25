# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:52:18 2021

@author: Fenrir

Description :


Variable:
    
Algorithm/Calculation:
"""
import random
"""
list_a = [random.randint(1, 101) for x in range(8)]
list_b = [random.randint(-100, 0) for x in range(6)]
"""
list_a = []
list_b = []
for x in range(8):
    list_a.append(random.randint(1, 101))
for x in range(6):
    list_b.append(random.randint(-100, 0))


list_c = list_a.copy()
list_c.extend(list_b)
print("list_a:", list_a)
print("list_b:", list_b)
print("list_c:", list_c)

print("------ sort ------")
list_a.sort()
list_b.sort(reverse = True)
print("list_a:", list_a)
print("list_b:", list_b)

print("------ max - min ------")
pop_max = list_c.pop(list_c.index(max(list_c)))
pop_min = list_c.pop(list_c.index(min(list_c)))
print("list_c:", list_c)
print(f"{pop_max} - {pop_min} = {pop_max - pop_min}")
