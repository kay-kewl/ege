def f(a, b, flag):
    if a == b:
        return 1
    if a > b:
        return 0
    if flag:
        return f(a+1, b, True) + f(a+2, b, True) + f(a * 2, b, False) + f(a * 3, b, False)
    return f(a+1, b, flag) + f(a+2, b, flag)


print(f(1, 11, True))