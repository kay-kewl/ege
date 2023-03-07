P = range(17, 47)
Q = range(22, 58)
m = []
for a1 in range(10, 60):
    for a2 in range(a1 + 1, 60):
        count = 0
        A = range(a1, a2)
        for x in range(1000):
            if (not (x in A)) <= (((x in P) and (x in Q)) <= (x in A)):
                count += 1
        if count == 1000:
            print(A, len(A))
            m.append(A)
print(len(sorted(m, key=len)[0]) - 1)

lst = []
for i in P:
    if i in Q:
        lst.append(i)
print(lst, len(lst))

