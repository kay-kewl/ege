print('w x y z')
F = lambda w, x, y, z: (w or (not x)) and (w == (not y)) and (w <= z)
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if F(w, x, y, z):
                    print(w, x, y, z)

# w - z x