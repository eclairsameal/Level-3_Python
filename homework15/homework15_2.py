# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 18:16:04 2021

@author: Fenrir

Description :

インターネットのとあるサービスで利用するためのハンドルネームを作ることにしました。
そのハンドルネームは名前の文字列から母音を取り除いて子音のみを連結して生成します。

ただし、ここで母音とは “a”, “e”, “i”, “o”, “u” の 5 つのアルファベットの小文字( “a”, “e”, “i”, “o”, “u” )、
大文字( “A”, “E”, “I”, “O”, “U” )を指し、子音とはそれ以外のアルファベットを意味します。
"""
# if and or 
input_line = input()
output_str = ""
for c in input_line:
    if c=="a" or c == "e" or c == "i" or c == "o" or c == "u" or c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
        output_str+=""
    else:
        output_str+= c
print(output_str)  
      
"""

# remove()
output_str = list(input())
remove_char = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
for rc in remove_char:
    while rc in output_str:
        output_str.remove(rc)
str1 = ''.join(output_str) # List to string
print(str1)

# c in remove_char
input_line = input()
remove_char = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
output_str = ""
for c in input_line:
    if c in remove_char: 
        output_str+=""
    else:
        output_str+= c
print(output_str)

# not c in remove_char
input_line = input()
remove_char = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
output_str = ""
for c in input_line:
    if not c in remove_char: 
        output_str+= c
print(output_str)

# funcion and map
def fun(c):
    remove_char = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if c in remove_char: 
        return ""
    else:
        return c
str1 = ''.join(list(map(fun, input_line))) # List to string
print(str1)

"""