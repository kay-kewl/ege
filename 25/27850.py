for n in range(245690, 245757):
    count = 0
    for x in range(2, int(n ** 0.5)):
        if n % x == 0:
            count += 2
    if n % (n ** 0.5) == 0:
        count += 1
    if count == 0:
        print(n - 245690 + 1, n)
