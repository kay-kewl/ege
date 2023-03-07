a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for p in range(10, 34):
    b = a[1:p]
    for x in b:
        for y in b:
            if int(x * 3 + '8', p) + int(f'43{x}9', p) == int(y * 2 + '04', p):
                print(p, x, y)
print(13 * 13 * 10 + 136)