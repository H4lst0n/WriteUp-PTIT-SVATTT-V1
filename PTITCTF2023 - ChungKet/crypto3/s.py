from pwn import *
from mt19937predictor import MT19937Predictor

predictor = MT19937Predictor()
r = remote("159.223.44.154", 8989)
for i in range(624):
    r.recvuntil(b"Your choice:")
    r.sendline(b"1")
    predictor.setrandbits(int(r.recvline().decode().strip()), 32)
r.recvuntil(b"Your choice:")
r.sendline(b"2")
enc = eval(r.recvline().decode().strip())
flag = ""
for i in enc:
    flag += chr(i - predictor.getrandbits(32))
print(flag)