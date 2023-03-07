for n in range(210235, 210301):
    count = 0
    lst = []
    for x in range(2, int(n ** 0.5)):
        if n % x == 0:
            count += 2
            lst.append(n // x)
            lst.append(x)
    if n % (n ** 0.5) == 0:
        count += 1
    if count == 4:
        print(n)
        print(lst)