def f(n, m):
    return n % m == 0


for A in range(1, 1000):
    count = 0
    for x in range(1, 1001):
        if f(A, 45) and (f(750, x) <= ((not f(A, x)) <= (not f(120, x)))):
            count += 1
    if count == 1000:
        print(A)
        break