for n in range(1, 1000):
    s = bin(n)[2:]
    if n % 3 == 0:
        s = s + s[-3:]
    else:
        s = s + bin((n % 3) * 3)[2:]
    s = int(s, 2)
    if s > 76:
        print(n)
        break