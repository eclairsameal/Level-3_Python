# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 19:49:04 2020

@author: Fenrir

Description :
- １～１００の間に存在する素数を全て出力し表示して下さい。
- 数値と数値の間は1マスの空白で区切る事
Variable:

"""

# 方法1 - bool変数
for i in range(2, 101):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i, end = " ") 
print() 
            
# 方法2 - forループのelse
"""
elseブロックが処理されるのは、「breakでループを抜けなかった時」です。
補足すると「ループを一度も実行しなかった時」も含まれます。
"""
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0: # 割り切れるので素数ではありません
            break
    else: # 2番目のループが終了する前に中断がない場合
        print(i, end = " ") 
print() 

# *方法3 - List Comprehensions and all() function
result = [x for x in range(2, 101) if all(x % i for i in range(2, x))]
print(result)

"""
all(）:
iterable（リストのようなデータ）のすべての要素が true の場合、trueを返します。
x ％ i の数が 0 である限りは false を意味し、 0 でない場合は true を意味します。
"""
"""
all_x = 7    # 素数
all_x = [all_x % i for i in range(2, all_x)]
print(all_x)     # [1, 1, 3, 2, 1] 
print(all(all_x))     # True

all_x = 10    # not素数
all_x = [all_x % i for i in range(2, all_x)]
print(all_x)     # [0, 1, 2, 0, 4, 3, 2, 1] 0があります
print(all(all_x))     # False
"""