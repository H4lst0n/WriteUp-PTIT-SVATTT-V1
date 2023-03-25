import pandas as pd

a = []
b = []
f = open("d:/svatttptit2023/crypto2/x.txt", "r")
for line in f:
    line = line.strip() # remove leading/trailing whitespace
    if line not in a:
        a.append(line)
        b.append(1)
    else:
        b[a.index(line)] += 1

sum = 0
for i in b:
    sum += i
print(sum)

d = ["R", "T", "E", "A", "O", "L", "N", "S", "I", "C", "U", "D", "P", "M", "H", "G", "B", "F", "Y", "W", "K", "V", "X", "Z", "J", "Q", "_", " ", "-", "{", "}", "."]  # Add 4 more elements to match the length of a, b, and c

c = []
for i in b:
    c.append(i / sum * 100)

df = pd.DataFrame({'Ciphertext' : a, 'Appear' : b, 'Frequency': c})
df = df.sort_values('Appear', ascending=[False])
df['Alphabet'] = d
print(df)