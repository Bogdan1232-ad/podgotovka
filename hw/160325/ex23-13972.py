def f(x, y, con):
    if x == y:
        return 1
    if x > y:
        return 0
    if con == 0:
        return f(x + 2, y, 1) + f(x * 2, y, 1)
    return f(x + 2, y, 1) + f(x * 2, y, 1) + f(x + 5, y, 1)
print(f(7, 23, 0) * f(23, 35, 1))