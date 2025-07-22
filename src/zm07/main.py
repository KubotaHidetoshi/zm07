import datetime

import typer

from zm07 import mathtools

from . import demo
from . import rain


import re
from datetime import datetime

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


