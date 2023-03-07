P = range(12, 63)
Q = range(52, 93)
m = []
for a1 in range(10, 100):
    for a2 in range(a1 + 1, 100):
        count = 0
        A = range(a1, a2)
        for x in range(1000):
            if (not (not (x in A) and (x in P))) or (x in Q):
                count += 1
        if count == 1000:
            print(A, len(A))
            m.append(A)
print(len(sorted(m, key=len)[0]))

