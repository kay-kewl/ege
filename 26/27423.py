with open('files/26_demo.txt') as file:
    data = file.readlines()

disk, n = data.pop(0).split()
disk, n = int(disk), int(n)
data = [int(x) for x in data]
data.sort()
lst = []
print(data)
for i in data:
    if sum(lst) + i > disk:
        print(len(lst))
        print(sum(lst[:567]))
        print(data[567:])
        break
    lst.append(i)