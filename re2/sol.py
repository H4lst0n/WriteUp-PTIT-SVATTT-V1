import subprocess
import re

flag =b"xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
f = [None] * 29
file = open("save.txt", "w")
for i in range(32,128):                                 #brute force (if array[i] == 0 ---> array[i] = 32-128)
    payload = flag.replace(b"x", chr(i).encode("ascii"))
    process = subprocess.Popen(["easyRE.exe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)       ##open file easyRE
    process.stdout.read(36)                             #read 36 bytes stdout
    process.stdin.write(payload + b"\r\n")              #write flag stdin
    process.stdin.flush()
    process.stdout.read(7)                              #read 7 bytes stdout remove color "\x1b[35m"
    char = process.stdout.read(1)                       #read 1 byte (array check number)
    while(char!=b"]"):                                  #compare "]" to remove "\x1b[0m"
        file.write(char.decode("ascii"))                #write array to .txt
        char = process.stdout.read(1)
    file.write("\n")
file.close()

with open("save.txt", "r") as file:                     #read file saved
    cnt = 32
    for line in file:
      lines = line.strip().split()                      #split elements
      i = 0
      for word in lines:
        if(int(word) == 0):                             #element == 0 --> save to array 
          f[i] = cnt
        i+=1
      cnt+=1
real_flag = ""
for i in f:
  real_flag += chr(i)
print(f'ATTT{{{real_flag}}}')
