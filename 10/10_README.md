# Week 10

矩形データを扱う。Python の言語機能を超えて、個別のサードパーティライブラリとその連携方法を覚えていきます。

```bash
uv add pandas seaborn openpyxl yfinance pandas-datareader
```

- pandas: 矩形データの処理（数値計算ライブラリ numpy もインストールされる）
- seaborn: データ可視化 (matplotlib もインストールされる)
- openpyxl: pandas で XLSXファイルを読み込むのに必要
- yfinance: Yahoo ファイナンスからデータ取得
- pandas-datareader: いろんなデータソースから経済データの取得


Pandas の矩形データは DataFrame と呼ばれます。その他のライブラリ（今とくに有力な代替ライブラリは polars）やその他の言語（R、Julia）でも data frame という言葉が使われるので覚えておきましょう。形状は Excel の1シートのような形状です。


|       | Column 1  | Column 2  | Column 3  |
| ----- | --------- | --------- | --------- |
| Row 1 | value 1,1 | value 1,2 | value 1,3 |
| Row 2 | value 1,1 | value 1,2 | value 1,3 |
| Row 3 | value 1,1 | value 1,2 | value 1,3 |
| Row 4 | value 1,1 | value 1,2 | value 1,3 |


## tidy data

tidy なデータという考え方があります。データを記録するときは、次のようにレイアウトするというものです。

- 1つの列は1つの変数
- 1つの行は1回の観測

例えば、成績データを入力するときには次のようにするのが自然でしょう。


| Student | Math | English |
| ------- | ---- | ------- |
| Alice   |      |         |
| Bob     |      |         |
| Charlie |      |         |
| David   |      |         |


## DataFrame の生成

Pandas は慣習的に

```
import pandas as pd
```

というコードでインポートします。以下、　`pd` は pandas のことです。


### 手作業で作る

`pd.DataFrame()` を使います

- 10/10a.py 
- 10/10b.py



### 基本的な操作

データフレームからデータを読み取るのは

- 列を選択する (10c.py, 10d.py)
- 行をフィルターする (10e.py)
- その組み合わせ (10f.py)

が基本です。さらに、次の操作もよく行われます。

- 列を追加する
- 特に、1つまたは複数の列の計算結果から新たな列を追加する (10g.py)

さらに、

- グループ化してグループ内での計算を行う


## ファイルから読み取る
