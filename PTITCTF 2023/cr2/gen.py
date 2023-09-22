import random

emojis = ["😭", "😰", "😱", "😡", "😝", "😘", "😍", "😉", "😃", "😂", "😋", "😤", "😣", "😵", "😔", "😅"]
m = open("text.txt", "rb").read().hex()

random.shuffle(emojis)

for e, c in zip(emojis, "0123456789abcdef"):
    m = m.replace(c, e)

open("out2.txt", "w", encoding="utf-8").write(m)
