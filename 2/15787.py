print('w x y z')
F = lambda w, x, y, z: ((x <= y) and (y <= w)) or (z == (x or y))
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not F(w, x, y, z):
                    print(y, w, z, x)
# y w z x