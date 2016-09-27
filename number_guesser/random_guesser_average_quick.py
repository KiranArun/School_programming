import random
r = 0
for z in range(1000000):
    s = random.randint(0,100)
    lb = 0
    hb = 100
    rn = random.randint(lb, hb)
    x = 0
    while True:
        x += 1
        if rn < s:
            lb = rn + 1
            rn = random.randint(lb, hb)
        elif rn > s:
            hb = rn - 1
            rn = random.randint(lb, hb)
        elif rn == s:
            break
    r = r + x

print(r/1000000)
