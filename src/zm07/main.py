import datetime
import typer

from zm07 import mathtools

from . import demo
from . import rain

from datetime import datetime

import re
from datetime import datetime
import random

app = typer.Typer()


@app.callback()
def callback():
    """
    A Collection of Useful Commands
    """


@app.command()
def now():
    """
    Show local date and time
    """
    today = datetime.today()
    typer.echo(today.strftime('%A, %B %d, %Y'))


@app.command()
def gcd(x: int, y: int):
    """
    Greatest Common Divisor
    """
    typer.echo(mathtools.gcd(x, y))


@app.command()
def high(m,n):
    "大きい数字"
    if m<n:
        m=n
    return m

@app.command()
def average(m,n):
    "平均"
    return (m+n)/2

@app.command()
def lcm(x:int,y:int):
    """最小公倍数"""
    typer.echo(mathtools.lcm(x,y))


@app.command()
def hello(name: str = "Hidetoshi"):
    typer.echo(demo.hello(name))

@app.command()
def get_rain_probability():
    """降水確率"""
    prob = rain.get_rain_probability()
    
    if prob is None:
        typer.echo("取得失敗")
        return
    
    typer.echo(f"{prob}%")



@app.command()
def pick_random_seiza(file_name="seiza.xlsx", column_index=0):
    """
    同じフォルダ内のExcelファイルからランダムに星座を1つ選ぶ関数

    Parameters:
    - file_name (str): Excelファイル名（デフォルトは 'seiza.xlsx'）
    - column_index (int): 読み込む列のインデックス（通常は0）

    Returns:
    - str: ランダムに選ばれた星座
    """
    # Excelファイルを読み込む
    df = pd.read_excel(file_name, engine='openpyxl')
    
    # 指定された列から星座リストを取得
    seiza_list = df.iloc[:, column_index].dropna().tolist()
    
    # ランダムに1つ選んで返す
    return random.choice(seiza_list)

@app.command()
def hoshi():
    seiza = [
        "牡羊座", "牡牛座", "双子座", "蟹座", "獅子座", "乙女座",
        "天秤座", "蠍座", "射手座", "山羊座", "水瓶座", "魚座"
    ]

    print("今日のラッキー星座は：", random.choice(seiza))
if __name__ == "__main__":
    hoshi()