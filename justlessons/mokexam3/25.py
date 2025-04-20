def f(num):
    l = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            l.add(i)
            l.add(num // i)
    if l == set():
        return 0
    return max(l) - min(l)

cou = 0
for i in range(300_000, 1_000_000):
    s = f(i)
    if str(s)[-1] == '6':
        print(i, s)
        cou += 1
    if cou == 6:
        break
