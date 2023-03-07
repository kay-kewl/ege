with open('22.txt') as file:
    data = file.readlines()

a = []
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in data:
    for n in range(30, 2, -1):
        for letter in abc:
            if i.count(letter * n) > 0:
                a.append([i.count(letter), i.count(letter * n), n])
print(sorted(a, key=(lambda x: x[2])))
