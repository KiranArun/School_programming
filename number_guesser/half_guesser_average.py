
import random
r = 0
for z in range(100):
    s = random.randint(1,100)
    x = lb = 0
    hb = 100
    y = 50
    print('think of a number between 0 and 100, h for higher, l for lower, c for correct')
    print(s)
    while True:
        x += 1
        if y < s:
            print(y, 'small')
            lb = y
            y= round((hb+lb)/2)
        elif y > s:
            print(y, 'big')
            hb = y
            y= round((hb+lb)/2)
        elif y == s:
            print('took', x, 'attemps')
            break
    r = r + x

print(r/100)
