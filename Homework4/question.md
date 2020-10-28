## 問題 1：整数の指定されたフォーマットでの表示
### プログラム説明：

次に記述するフォーマットと同様のプログラムを作成する。
実行後４つの整数を入力でき、それらの整数を表示する際に５つのスペースを使い、整数と整数の間にスペースを１つ空けておく事。
そして1列に付き２つの整数を表示し、先ず右揃えで4つの整数を表示させ、その後左揃えで4つの整数を表示する事。
1列の始まりと終わりの際、|（バーティカルバー）を使い1列1列の境界とする事。

### 入出力説明：
入力説明:４つの整数

表示説明:指定されたフォーマットで表示

### 入力例:

```
85
4
299
478
```
### 表示例:

```
|   85     4|
|  299   478|
|85    4    |
|299   478  |
```

[Code example - F](https://github.com/eclairsameal/Level-3_Python/blob/main/Homework4/Fenrir/Homework4_1.py)

[Code example - F(use List)](https://github.com/eclairsameal/Level-3_Python/blob/main/Homework4/Fenrir/Homework4_1(list).py)

## 問題 2：文字列を指定したフォーマットで表示

### プログラム説明：
次のプログラムを作成せよ。 4つの英単語を入力し、これらの単語に10スペースを用い、単語同士の間に1つスペースを置く。 列ごとに2つの単語を表示し、先に右揃えで表示した後に、左揃えで表示させること。 列の始めと終わりは、|（バーティカルバー）を用いて境界とすること。

### 入出力説明：

入力説明: ４つの英単語
出力説明: 指定されたフォーマットで表示

### 入力例:

```
I
enjoy
learning
Python
```
### 表示例:

```
|         I      enjoy|
|  learning     Python|
|I          enjoy     |
|learning   Python    |
```

[Code example - F](https://github.com/eclairsameal/Level-3_Python/blob/main/Homework4/Fenrir/Homework4_2.py)

[Code example - F(use List)](https://github.com/eclairsameal/Level-3_Python/blob/main/Homework4/Fenrir/Homework4_2(list).py)


## 問題 3：矩形面積の計算
### プログラム説明：
次のプログラムを作成せよ。 2つの正数を入力し、片方は高さ、片方は幅とし、 これらを用い矩形の面積を算出する事。 表示する際は、高さ（Height）、幅（Width）、周りの長さ（Perimeter）、そして面積（Area）を表示する事。

補足：小数を表示する際、小数以下は2桁に留める事。

### 入出力説明：
入力説明: 高さ、幅

出力説明: 高さ、幅、周りの長さ、面積

### 入力例:

```
23.5
19
```
### 表示例:

```
Height = 23.50
Width = 19.00
Perimeter = 85.00
Area = 446.50
```

[Code example - F](https://github.com/eclairsameal/Level-3_Python/blob/main/Homework4/Fenrir/Homework4_3.py)

## 問題 3：正n角形の面積計算
### プログラム説明：
次のプログラムを作成せよ。 ユーザーに2つの正数（n、s）を入力させ、これらは「正　n　角形で辺は　s　」とする。 この数値を用い、正n角形の面積を算出する事。

正n角形の面積を求める公式：Area = (n * pow(s, 2))/(4 * tan(pi/n))

表示する際、小数点以下は4桁に留める事。

### 入出力説明：
入力説明: 正数n、s
出力説明: 正 n 角形の面積

### 入力例:

```
8
6
```
### 表示例:

```
Area = 173.8234
```

[Code example - F](https://github.com/eclairsameal/Level-3_Python/blob/main/Homework4/Fenrir/Homework4_4.py)
