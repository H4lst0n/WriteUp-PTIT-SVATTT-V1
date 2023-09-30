import random

flag = open("flag.txt", "r").read().strip()
for i in range(666):
    choice = input(
        "1.Get random number\n2.Get flag encrypted\nYour choice:").strip()
    if (choice == '1'):
        random_value = random.getrandbits(32)
        print(random_value)
    elif choice == '2':
        enc = []
        for char in flag:
            enc.append(ord(char) + random.getrandbits(32))
        print(enc)
