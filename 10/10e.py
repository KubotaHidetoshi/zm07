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

# 数学が 80点以上の行のみを表示する
min_val = 80

# 方法 1
print(df[df["数学"] >= min_val])

print()

# 方法 2
# 参考 https://note.nkmk.me/python-pandas-query/
print(df.query(f"数学 >= @min_val"))


print()

# 数学が80点以上、英語が70点以下
print(df[(df["数学"] >= 80) & (df["英語"] <= 70)])


# 色々なフィルタを試してみよう