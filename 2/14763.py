print('x y z')
F = lambda x, y, z: (x or y) <= (y == z)
for w in range(1):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not F(x, y, z):
                    print(x, y, z)

# z - y