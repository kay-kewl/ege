a = int(input())
q = set()
b = set()
while a >= 0:
    q.add(a)
    a = int(input())
a = int(input())
while a >= 0:
    b.add(a)
    a = int(input())
c = q - b
for i in c:
