# 2?1*67

for a in range(10):
    for b1 in range(10):
        for b2 in range(10):
            b = str(b1) + str(b2)
            s = f'2{a}1{b}67'
            if int(s) % 159 == 0:
                print(s)