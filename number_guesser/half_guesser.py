x = lb = 0
hb = 100
y = 50
print('think of a number between 0 and 100, h for higher, l for lower, c for correct')
q = str(input(y))
while True:
    x += 1
    if q == 'h':
        lb = y
        y= round((hb+lb)/2)
        q = str(input(y))
    elif q == 'l':
        hb = y
        y= round((hb+lb)/2)
        q = str(input(y))
    elif q == 'c':
        print('took', x, 'attemps')
        break
