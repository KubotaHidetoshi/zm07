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

# 数学と英語のデータだけを表示する
math_and_eng = df[["数学", "英語"]]
print(math_and_eng)

# 空行
print()

# 数学と英語の平均点を表示する
print(______)

print()

# 練習: いろんな代表値を表示してくれるメソッド describe()
print(df._______())