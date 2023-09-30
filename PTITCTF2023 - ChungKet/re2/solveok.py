import re
import warnings
from gmpy2 import iroot
from random import *

x = open("decompilee.py").read()

g = re.findall(r"(\[n for n in \(\)\.__class__\.__base__\.__subclasses__\(\) if \"rni\" in n\.__name__ and n\.__name__ == n\.__name__\.lower\(\)\]\[0\]\(\)\._module\.__builtins__\.__getitem__\(\".+?\"\),\"(.+?)\"\).decode\(\))",x)
for i in g:
    exec(f"w=bytes.fromhex(\"{i[1]}\")")
    x = x.replace(i[0],f"{w}")

g = re.findall(r"__getitem__\(b'globals'\)\(\)\.__getitem__\(b'inp'\)\.__getitem__\((\d+?\^\d+?)\)\.__pow__\((\d+?)\)\.__eq__\((\d+?)\)",x)
inp = bytearray([1]*51)
for i in g:
    inp[eval(i[0])]=int(iroot(eval(i[2]),eval(i[1]))[0]) # inp[3] = x**eval(i[1]) = eval(i[2]
print(inp.decode())

def stage2(b):
    seed(10)
    t = "++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++.++++++.-----------.++++++."[-15:(7*9)].strip('-')
    for q in range(0,len(b)):
        t += chr(ord(b[q])+randint(0,5))
    return t

def stage1(a):
    a = list(a)
    for o in range(len(a)):
        a[o] = chr(ord(a[o])^o)
    a.reverse()
    z = "".join(x for x in a)     
    return z

print(stage1(stage2(inp.decode())))