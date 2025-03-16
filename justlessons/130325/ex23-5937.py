def f(x, y, й):
    if x == y:
        return 1
    if x > y:
        return 0
    if x % 2 == 0:
        й += 1
    return f(x + 2, y, й) + f(x + 3, y, й) + f(x * 2 + 1, y, й)

print(f())