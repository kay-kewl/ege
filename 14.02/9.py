with open('9.txt') as file:
    data = file.readlines()

count = 0
for i in data:
    ns = [int(x) for x in i.split()]
    d = {}
    a = []
    b = []
    if 6 > len(set(ns)) > 1:
        for j in set(ns):
            d[j] = ns.count(j)
            if d[j] == 1:
                a.append(j)
            else:
                for _ in range(d[j]):
                    b.append(j)
        if b == [] or (a != [] and sum(a) / len(a) > sum(b) / len(b)):
            count += 1
print(count)
print(157 * 32768 / 2 ** 10)
