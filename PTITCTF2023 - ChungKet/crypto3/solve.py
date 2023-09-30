from pwn import *

p = remote("159.223.44.154", 8989)
output_content = ""

for i in range(666):
    p.sendline(b"2")
    received_data = p.recvline().decode('utf-8')
    output_content += received_data

p.interactive()

with open("output.txt", "w") as file:
    file.write(output_content)
