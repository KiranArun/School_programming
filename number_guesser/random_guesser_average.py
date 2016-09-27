import random
r = 0
for z in range(100):
    s = random.randint(1,100)
    lb = 0
    hb = 100
    rn = random.randint(lb, hb)
    print('think of a number between 0 and 100, h for higher, l for lower, c for correct')
    x = 0
    print(s)
    while True:
        x += 1
        if rn < s:
            print(rn, 'is lower')
            lb = rn + 1
            rn = random.randint(lb, hb)
        elif rn > s:
            print(rn, 'is higher')
            hb = rn - 1
            rn = random.randint(lb, hb)
        elif rn == s:
            print('took', x, 'attemps')
            break
    r = r + x

print(r/100)
