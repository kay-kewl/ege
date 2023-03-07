print('w x y z')
F = lambda w, x, y, z: ((not x) and (not y)) or (y == z) or (not w)
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not F(w, x, y, z):
                    print(z, y, x, w)