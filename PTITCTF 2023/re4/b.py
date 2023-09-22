from pwn import *
from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from tqdm import *

def lsbOracle(c):
    r.recvuntil(b"c = ")
    r.sendline(str(c).encode())
    r.recvuntil(b"Result: ")
    m = r.recvline().strip()
    return int(m)


for j in tqdm(range(5)):
    check = 0
    r = remote("128.199.247.205", 6989)
    r.recvuntil(b"flag_enc = ")
    flag_enc = int(r.recvline().strip())
    r.recvuntil(b"e = ")
    e = int(r.recvline().strip())
    r.recvuntil(b"n = ")
    n = int(r.recvline().strip())
    r.recvuntil(b"Length: ")
    length = int(r.recvline().strip())
    flag = str(j)
    print(int(flag, 5))
    for i in tqdm(range(1, length + 10, 1)):
        inv = inverse(5*i, n)
        chosen_ct = (flag_enc - pow(inv, e, n) % n)
        output = lsbOracle(chosen_ct)
        flag_char = (output - (int(flag, 5) * inv) % n) % 5
        flag = str(flag_char) + flag
        try:
            if (b"PTITCTF{" in long_to_bytes(int(flag, 5))):
                print(long_to_bytes(int(flag, 5)))
                check = 1
                break
        except:
            pass
    if (check == 1):
        r.close()
        break
