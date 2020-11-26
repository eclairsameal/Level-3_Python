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

[Code example - F](https://github.com/eclairsameal/Level-3_Python/blob/main/Homework7/Fenrir/Homework7_1.py)

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

[Code example - F](https://github.com/eclairsameal/Level-3_Python/blob/main/Homework7/Fenrir/Homework7_2.py)

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

[Code example - F](https://github.com/eclairsameal/Level-3_Python/blob/main/Homework7/Fenrir/Homework7_3.py)


## 4. ユーザーに身長と体重を入力させ、BMIを測定し且次の表からBMIの範囲内に記載されているコメントを入出力例を参考にしてプログラムを作成してください。

1. 入力は身長（cm）と体重(kg)

2. 出力時は、「Your BMI is ○○.」、そして「comment: ××」と表示する（○○→BMI数値（小数点以下2桁まで計算）、××→コメントの内容）

| BMI | コメント |
| -------- | -------- |
| 18.49以下 | Underweight |
| 18.50〜24.99以下 | Normal weight |
| 25.00〜29.99以下 | Overweight |
| 30.00以上 | Obese |


### 入力と表示例

[Code example - G](https://github.com/eclairsameal/Level-3_Python/blob/main/Homework7/George/Homework7_4.py)

## 5. ある選手が400メートル走をしようとしています。この選手は時速「Y」キロメートルで走っています。走り始めてから400メートル走り終えるまでずっと同じ速度だと仮定します。400メートルでかかる時間を結果として出力し、次の条件を満たすプログラムを作成してください。

1. 入力：時速「Y」キロメートル
     - Please input speed (km/h):
     
2. 出力：時速「Y」キロメートルにより400メートルにかかった時間
     - Spend time: ○○ sec
     
3. かかった時間が10秒以内である場合は、「Invalid」と出力する事

### 入力と表示例

[Code example - G](https://github.com/eclairsameal/Level-3_Python/blob/main/Homework7/George/Homework7_5.py)
