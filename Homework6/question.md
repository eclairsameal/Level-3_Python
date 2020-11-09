# Homework 6

## 1. 次の要求を満たすプログラムを作成してください。

1. 数字を1つ入力することが出来る

2. 入力した数字が奇数であれば「Odd number」と出力する

3. 入力した数字が偶数であれば「Even number」と出力する

![](https://i.imgur.com/qKZfhQj.png)    

### 入力と表示例:

```
Input a number: 10
10 is an Even number.

Input a number: 7
7 is an Odd number.
```

[Code example - F](https://github.com/eclairsameal/Level-3_Python/blob/main/Homework6/Fenrir/Homework4_1.py)

## 2. 次の要求を満たすプログラムを作成してください。

1. ユーザーに月数を入力させることが出来る

2. 入力した月数を下の表にそって該当季節を出力する
    
| 月数（月） | 季節 | 出力 |
| -------- | -------- | -------- |
| 4、5、6 | 春 | Spring |
| 7、8、9 | 夏 | Summer |
| 10、11、12 | 秋 | Autumn |
| 1、2、3 | 冬 | Winter |
        
![](https://i.imgur.com/qcLsJ4A.png)

### 入力と表示例:

```
Please input month: 7
Summer

Please input month: 2
Winter

Please input month: 8
Summer

Please input month: 12
Autumn

```

[Code example - F](https://github.com/eclairsameal/Level-3_Python/blob/main/Homework6/Fenrir/Homework4_2.py)

## 3. ユーザーに数字（西暦）を入力させ、閏年であるかを判断することが出来るプログラムを作成してください。判断基準は以下の通り：

1. 数字が4の倍数であればその年は閏年「leap year」と表示

2. 但し数字が100の倍数であれば2.よりも優先されその年は平年「Normal year」と表示

3. 更に数字が400の倍数であれば3.よりも優先されその年は閏年「leap year」と表示

![](https://i.imgur.com/gxI4hgS.png)

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

[Code example - F](https://github.com/eclairsameal/Level-3_Python/blob/main/Homework6/Fenrir/Homework4_3.py)

## 4. ユーザーに数字を入力させ、その数字が2や3で割り切れるかどうかを判断できるプログラムを作成してください。

1. 2で割り切れる場合「Multiple of 2」

2. 3で割り切れる場合「Multiple of 3」

3. 2と3同時に割り切れる場合「Multiple of 2 and 3」

4. どちらも割り切れない場合「Not multiple of 2 and 3」

### 入力と表示例:

```
Input a number: 6
6 is a multiple of 2 and 3.

Input a number: 7
7 is not a multiple of 2 or 3.

Input a number: 9
9 is a multiple of 3.

Input a number: 4
4 is a multiple of 2.

```

![](https://i.imgur.com/jA9aVUO.png)

[Code example - F](https://github.com/eclairsameal/Level-3_Python/blob/main/Homework6/Fenrir/Homework4_4.py)

これより以下難易度上昇
---

## 5. 某スーパーがイベントをしていて、次の表にそって即時キャッシュバックが発生します。
    | 小計（円） | キャッシュバック（円） |
    | -------- | -------- |
    | 3000～5999 | 300 |
    | 6000～9999 | 800 |
    | 10000～ | 1500 |
    もし今回スーパーに15000円を持って行ったとしましょう。次の条件を満たすプログラムを作成してください。
    1. 小計（円）を入力出来るようにすること（＜15000）
    2. 表を参考にして判断させ、支払いが済んだ後キャッシュバックされたお金も即時持って帰り所持金に加算する
    3. 買い物が済んだ時の残金を次のように表示させること「xxxxx yen」（xxxxx　は所持金額）

![](https://i.imgur.com/oa8lLAf.png)


## 6. 某先生は最終成績を出す際に次のルールに沿って再計算を行うことがあります。
    1. 成績はA、B、Cがありこれらを平均した数値が最終成績になる
        - Aは授業態度成績
        - Bは抜き打ちテストの平均成績
        - Cは期末試験の成績
    2. 最終成績が合格点以下（60点未満）だった場合、成績Aを次の公式で修正し新たな成績Aにする
        - 新たな成績A = (math.sqrt(旧成績A))*10

    上記のルールに従って次のプログラムを作成してください。
    1. 成績A、成績B、成績Cを入力出来るようにする
    2. これらの平均が合格点かどうか判断し合格であればそのまま平均点と合格を次の様に表示「XX point :Pass」
    3. もし不合格の場合、前述の方法にて「成績A」のみを再計算して再度平均点を算出し、合格か不合格を次の様に表示「XX point :Failure」
        補足：尚XXのポイントの小数点は切り上げて表示させること
        
![](https://i.imgur.com/TexhoSr.png)


### 入力と表示例:

```
Please input examA: 10
Please input examB: 80
Please input examC: 60
58 point: Failure

Please input examA: 36
Please input examB: 60
Please input examC: 60
60 point: Pass


Please input examA: 60
Please input examB: 80
Please input examC: 100
80 point: Pass

```

