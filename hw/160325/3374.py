def f(x, y, l=None):
    if l is None:
        l = set()
    if x == y:
        return 1
    if x in l or x <= -50 or x >= 50:
        return 0

    new_l = l.copy()
    new_l.add(x)

    return f(x + 2, y, new_l) + f(x - 3, y, new_l)


print(f(1, 30, set()))
