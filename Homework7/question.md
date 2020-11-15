# Homework 6

## 1. 三角形判断
次の条件を満たすプログラムを作成せよ。 

1. ユーザーに3つの辺を入力させ、それらの辺で1つの三角形として成り立つかどうかを判断する事。
     
2. もし出来る場合は三角形の周りの長さの値を、出来ない場合は【Invalid】と表示する事。
    
3. プログラムは「and」や「or」を使う事
    
補足：三角形の判断方法　→　3つの内いずれ2つの辺の合計が残りの1つの辺より大きくなければならない。 

### 入力と表示例:

```
Input a:4
Input b:5
Input c:6
15

Input a:1
Input b:2
Input c:6
Invalid
```

[Code example - F]()

## 2. 次の要求を満たすプログラムを作成してください。

1. ユーザーに月数を入力させることが出来る

2. 入力した月数を下の表にそって該当季節を出力する

3. 範囲外の数値が入力された場合、「○○ not in range.」と表示する(○○は入力された数値)、範囲外の数値判断は「or」を使う事。
  
| 月数（月） | 季節 | 出力 |
| -------- | -------- | -------- |
| 4、5、6 | 春 | Spring |
| 7、8、9 | 夏 | Summer |
| 10、11、12 | 秋 | Autumn |
| 1、2、3 | 冬 | Winter |
        

### 入力と表示例:

```
Please input month: 15
15 not in range.

Please input month: 0
0 not in range.

Please input month: 2
Winter

Please input month: 8
Summer

Please input month: 12
Autumn

```

[Code example - F]()

## 3. ユーザーに数字（西暦）を入力させ、閏年であるかを判断することが出来るプログラムを作成してください。判断基準は以下の通り：

1. 数字が4の倍数であればその年は閏年「leap year」と表示

2. 但し数字が100の倍数であれば2.よりも優先されその年は平年「Normal year」と表示

3. 更に数字が400の倍数であれば3.よりも優先されその年は閏年「leap year」と表示

4. プログラムは「and」と「or」を使って、判断式を一行で終わらせること（1行で全ての判断を書き込むこと）

### 入力と表示例

```
Please input year:2000
2000 is a leap year.

Please input year:1900
1900 is a normal year.

Please input year:1992
1992 is a leap year.

Please input year:1997
1997 is a normal year

```

[Code example - F]()