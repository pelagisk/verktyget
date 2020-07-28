from src.a import *

def b(x):
    if isinstance(x, list):
        x.append(x)
    else:
        x = [x]

o = list(str(A("hej axel!")))
b(o) # test av b
print(o)
