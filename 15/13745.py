for A in range(1000, 0, -1):
    count = 0
    for x in range(100):
        for y in range(100):
            if ((x <= 9) <= (x * x <= A)) and ((y * y <= A) <= (y <= 9)):
                count += 1
    if count == 10000:
        print(A)
        break