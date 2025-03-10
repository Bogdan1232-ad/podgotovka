def f(num):
    l = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            if i % 2 == 1:
                l.add(i)
            if (num // i) % 2 == 1:
                l.add(num//i)
    return sorted(l)
for n in range(200_000_001, 10**20):
    if len(f(n)) >= 6:
        print(n, f(n)[5])