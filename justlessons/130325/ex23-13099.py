def f(x, y, A):
    if x == y:
        return 1
    if x > y + 1:
        return 0
    if A != 1:
        return f(x - 1, y, 1) + f(x * 2, y, 0) + f(x * 3, y, 0)
    return f(x * 2, y, 0) + f(x * 3, 0, 0)

print(f(3, 15, 0))


