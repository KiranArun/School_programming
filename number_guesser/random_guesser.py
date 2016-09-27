import random
lb = 0
hb = 100
rn = random.randint(lb, hb)
print('think of a number between 1 and 100, h for higher, l for lower, c for correct')
q = str(input(rn))
x = 0
while True:
    x += 1
    if q == 'h':
        lb = rn + 1
        rn = random.randint(lb, hb)
        q = str(input(rn))
    elif q == 'l':
        hb = rn - 1
        rn = random.randint(lb, hb)
        q = str(input(rn))
    elif q == 'c':
        print('took', x, 'attemps')
        break
    
