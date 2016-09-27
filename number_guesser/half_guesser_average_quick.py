import random
r = 0
for z in range(1000000):
    s = random.randint(1,100)
    x = lb = 0
    hb = 100
    y = 50
    while True:
        x += 1
        if y < s:
            lb = y
            y= round((hb+lb)/2)
        elif y > s:
            hb = y
            y= round((hb+lb)/2)
        elif y == s:
            break
    r = r + x

print(r/1000000)
