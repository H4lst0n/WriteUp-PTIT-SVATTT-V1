from z3 import *

target = [0x01, 0x21, 0x31, 0x7d, 0x1d, 0x5d, 0x07, 0x01, 0x63, 0x6e, 0x35, 0x5f, 0x4b, 0x23, 0x7e]
#[BitVec("v%i"%i, 8) for i in range(len(target))]
flag = [BitVec("flag%i"%i, 8) for i in range(len(target))]
key = BitVec("key", 8)

s = Solver()

xorvalue = []
for i in range(len(target)):
    xorvalue.append(0)

for i in range(2606):
    for j in range(len(flag)):
        xorvalue[j] = flag[j] ^ key
        key = flag[j]
        flag[j] = xorvalue[j]

s.add(flag[0] <= 127 )
for i in range(len(target)):
    s.add(flag[i] <= 127)
    s.add(xorvalue[i] == target[i])
    

if s.check() == sat:
    m = s.model()

    print(m)
