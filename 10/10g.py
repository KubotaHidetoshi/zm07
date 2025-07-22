import pandas as pd

# サンプルデータの作成（辞書で表を作る）
data = {
    '名前': ['佐藤', '鈴木', '高橋', '田中'],
    '国語': [80, 90, 70, 60],
    '数学': [75, 85, 95, 50],
    '英語': [90, 60, 85, 70]
}

# DataFrameの作成
df = pd.DataFrame(data)

# 各生徒の平均点（横軸方向に平均を取る axis=1）
print(df.mean(axis=1, numeric_only=True))


# 列を追加する
df["平均"] = df.mean(axis=1, numeric_only=True)
print(df)


print()

# 色々な列を追加してみよう（合計、英数の平均など）


