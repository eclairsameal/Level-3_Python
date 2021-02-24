# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 14:12:45 2021

@author: Fenrir

Description :

"""
# -------------------- not function --------------------
ssn_str = input("Input: ").split()
for i in range(len(ssn_str)):
    ssn_list = ssn_str[i].split('-')
    if ssn_list[0].isupper() and ssn_list[1].islower() and ssn_list[2].isdigit(): # すべての3つの条件が真であります
        print("{}: Valid SSN".format(ssn_str[i]))
    else:
        print("{}: Invalid SSN".format(ssn_str[i]))
        


# -------------------- function --------------------
def isssn(s): # s がフォーマットを満たしているかどうかを判断します
    ssn_list = s.split('-') # IMS-ml-765 = ['IMS', 'ml', '765']
    return ssn_list[0].isupper() and ssn_list[1].islower() and ssn_list[2].isdigit()

# main      
ssn_str = input("Input: ").split()
for i in range(len(ssn_str)):
    print("{}: Valid SSN".format(ssn_str[i])) if isssn(ssn_str[i]) else print("{}: Invalid SSN".format(ssn_str[i]))