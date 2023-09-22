v6 = bytearray(b"\x00" * 48) 

source = b"\x19\a\x19\x17\x0F\x01\x042+`1\x13d1\x16&#p(\n 0\f\x18\" &6&=\x0F\"\"1\x1D? $;/>04"

for i in range(len(source)):
    v6[i] = source[i]

s = "PTITCTF"
key = bytearray()

for i in range(7):
    xored_value = v6[i] ^ ord(s[i])
    key.append(xored_value % 256)

print(key.decode())


#PTITCTF{x0r_1s_us3d_by_Halston_and_vstxckr}