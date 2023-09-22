from Crypto.Util.number import *
from Crypto.PublicKey import RSA

flag = open("flag.txt", "r").read().strip()
flag = bytes_to_long(flag.encode())
key = RSA.generate(2048)
e = key.e
p = key.p
q = key.q
n = key.n
d = key.d
print("flag_enc = " + str(pow(flag, e, n)))
print("e = " + str(e))
print("n = " + str(n))
print("Length: " + str(len(bin(flag)[2:])))
limit = 100 + len(bin(flag)[2:])
for i in range(limit):
    try:
        c = int(input('c = '))
        m = pow(c, d, n)
        print("Result: " + str(m % 5))
    except:
        exit(0)
