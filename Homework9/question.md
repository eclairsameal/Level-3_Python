## 1. 次の条件を満たすプログラムを作成して下さい。
- 1～100から3の倍数であるが、5の倍数ではない数値を出力し、表示させること

##### 入出力例
```
3 6 9 12 18 21 24 27 33 36 39 42 48 51 54 57 63 66 69 72 78 81 84 87 93 96 99 
```


## 2. 次の条件を満たすプログラムを作成して下さい。
1. ユーザーに数値を一つ入力させ、入力された数値が0以下であれば再度入力させるようにする
2. 入力した数値を整数にし変数入れた後、その変数の値を自乗した結果を出力し、表示させること

##### 入出力例
```
# 出力例1
Please input number:3
9

# 出力例2
Please input number:4.3
25

# 出力例3
Please input number:-0.4
Can't input under 0.

Please input number:-5.6
Can't input under 0.

Please input number:0
Can't input under 0.

Please input number:0.5
1

```

## 3. 次の条件を満たすプログラムを作成して下さい。
1. ユーザーに数値を入力させ、それが素数であるかを判断させる
2. 素数である場合はその数値をそのまま出力し表示させる
3. 素数でない場合はもう一度入力させ素数を入力するまで繰り返す

##### 入出力例
```
# 出力例1
Please input number:23
The number 23 is a prime number.

# 出力例2
Please input number:223
The number 223 is a prime number.

# 出力例3
Please input number:18
The number 18 is not a prime number.

Please input number again:97
The number 97 is a prime number.

```

## 4. 某スーパーで買い物をするとしてその会計機を作るとしましょう。商品は4種類ありそれぞれ番号で管理されています。商品番号とその値段は次の通りです。
- 1: 500
- 2: 800
- 3: 1600
- 4: 2200

以上の情報から次の条件を満たすプログラムを作成してください。
    1. ユーザーに商品番号を何度でも入力することが出来るようにする。
    2. 入力される度に、その時点での小計を表示する事。
    3. 入力された数値が0以下や商品が割り当てられている数字以外だった場合、その時点までの総額を表示させる。

```
# 出力例1
Please input item number:1
Item prise is 500.
Now total: 500 yen

Please input item number:3
Item prise is 1600.
Now total: 2100 yen

Please input item number:2
Item prise is 800.
Now total: 2900 yen

Please input item number:7
You have to pay: 2900 yen

# 出力例2
Please input item number:-1
You have to pay: 0 yen

```


## 5. 某コンビニが来客した人数を年齢に分けて数えようと思っています。分け方は次の通り：
- 0～17歳、18～39歳、40以上、の三種類に分けて数える

以上の分け方でプログラムを作成してください。
    1. ユーザーに年齢を何度でも入力することが出来るようにする。
    2. 年齢入力に0未満の数値が入力された場合集計を終了し、三種類各々出入りした人数を出力し、最後に出入りした人数の総数を出力する事

```
# 出力例1
Please input the customer's age:5

Please input the customer's age:19

Please input the customer's age:53

Please input the customer's age:23

Please input the customer's age:64

Please input the customer's age:-1
Today's cutomers info:
Age 0 to 17: 1
Age 18 to 40: 2
Age 40 or more: 2
Total customers: 5

# 出力例2
Please input the customer's age:5

Please input the customer's age:5

Please input the customer's age:5

Please input the customer's age:5

Please input the customer's age:5

Please input the customer's age:16

Please input the customer's age:23

Please input the customer's age:23

Please input the customer's age:-10
Today's cutomers info:
Age 0 to 17: 6
Age 18 to 40: 2
Age 40 or more: 0
Total customers: 8


```
