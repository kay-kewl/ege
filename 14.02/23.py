# mask = '1?7246*1'
#
# for v in range(10):
#     for z1 in range(10):
#         for z2 in range(10):
#             for z3 in range(10):
#                 n = mask.replace('?', str(v)).replace('*', str(z1) + str(z2) + str(z3))
#                 if int(n) % 4173 == 0:
#                     print(n)

for i in range(10 ** 4, 10 ** 8):
    s = '1' + str(i) + '1'
    if s[2:6] == '7246':
        if int(s) % 4173 == 0:
            print(s)
    s = f'10{i}1'
    if s[2:6] == '7246':
        if int(s) % 4173 == 0:
            print(s)
    s = f'100{i}1'
    if s[2:6] == '7246':
        if int(s) % 4173 == 0:
            print(s)
    s = f'1000{i}1'
    if s[2:6] == '7246':
        if int(s) % 4173 == 0:
            print(s)
