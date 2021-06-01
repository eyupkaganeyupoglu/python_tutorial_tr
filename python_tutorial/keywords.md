https://www.programiz.com/python-programming/keyword-list

from keywordu import, yield, raise

from random import radint

def üreteç1():
    yield "üreteç1 başladı" # 3
    yield "üreteç1 bitti" # 4

def üreteç2():
    yield "üreteç2 başladı" # 1
    yield from üreteç1() # 2 (üreteç1 direkt bitene kadar çalışır.)
    yield "üreteç2 bitti" # 5

try:
    print(i)
except NameError as NE:
    raise
