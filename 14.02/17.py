with open('17.txt') as file:
    data = [int(x) for x in file.readlines()]

m = min(filter(lambda x: x % 10 == 7, data)) ** 2
ms = 0
count = 0
for i in range(1, len(data)):
    a, b = data[i - 1], data[i]
    if a % 10 == b % 10 and ((a % 7 == 0 and b % 7 != 0) or (b % 7 == 0 and a % 7 != 0)):
        if a ** 2 + b ** 2 < m:
            count += 1
            ms = max(ms, a ** 2 + b ** 2)
print(ms, count)