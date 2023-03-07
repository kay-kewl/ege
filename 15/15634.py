for A in range(1, 1000):
    count = 0
    for x in range(100):
        for y in range(100):
            if (y + 2 * x < A) or (x > 30) or y > 20:
                count += 1
    if count == 10000:
        print(A)
        break