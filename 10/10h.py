import pandas as pd

# サンプルデータ
data = {
    '名前': ['佐藤', '鈴木', '高橋', '田中', '伊藤', '山本', '中村', '小林', '加藤', '斉藤'],
    '年齢': [23, 31, 19, 45, 27, 35, 41, 22, 30, 28],
    '職業': ['エンジニア', 'デザイナー', '学生', 'マネージャー', '営業',
           'エンジニア', 'デザイナー', '営業', '学生', 'エンジニア'],
    '給与': [500, 600, 0, 800, 550, 650, 580, 530, 0, 620]
}

# DataFrame の作成
df = pd.DataFrame(data)

# 職業ごとにグループ化して給与の平均を計算する

# 方法1: 平均を計算する関数 numpy.mean を使う
import numpy as np
print(df.groupby("職業")["給与"].apply(np.mean))


print()


# 方法2: ラムダ式（無名関数）を使う
print(df.groupby("職業")["給与"].apply(lambda x: x.mean()))


print()

# 結果を並べ替えるには次のようにする。ドットの後ろで改行しても OK
print(df.
      groupby("職業")["給与"].
      apply(np.mean).
      sort_values(ascending=False))


# 職業ごとの平均年齢を求めてみよう
