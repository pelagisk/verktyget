from src.a import *


def b(x):
    if isinstance(x, list):
        x.append(x)
    else:
        x = [x]
