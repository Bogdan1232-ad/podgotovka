def f(num):
    divs = set()
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divs |= {i}
            divs.add(num // i)
    divs = sorted(divs)
    if len(divs) <= 1:
        return 0

    return max(divs) + min(divs)


cou = 0
for i in range(800_000, 10 ** 100):
    if str(f(i)).endswith('4'):
        print(i, f(i))
        cou += 1
        if cou == 5:
            break
