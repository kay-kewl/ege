c = {}
for i in range(int(input())):
    a = input()
    x, y, z = a.split(maxsplit=2)
    if y in c:
        c[y].append((int(x), z))
    c[y] = c.get(y, [(int(x), z)])
b = input()
p = c[b]
c[b].sort()
print(p[0][1])