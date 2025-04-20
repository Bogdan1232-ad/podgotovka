def f(x, y):
    if x == y:
        return 1
    if x > y or x == 8:
        return 0
    return f(x + 1, y) + f(x * 2, y) + f(x * 5, y)

print(f(2, 27) * f(27, 54))