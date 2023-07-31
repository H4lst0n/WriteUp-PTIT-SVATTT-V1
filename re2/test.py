import subprocess
flag =b"xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
for i in range(32,128):
    payload = flag.replace(b"x", chr(i).encode("ascii"))
    process = subprocess.Popen(["EasyRE.exe"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    
    print(process.stdout.read(36))
    process.stdin.write(payload + b"\r\n")
    process.stdin.flush()
    char = process.stdout.read(1)
    while(char!=b"\n"):
        print(char.decode("ascii"), end="")
        char = process.stdout.read(1)
    print(" ", chr(i))