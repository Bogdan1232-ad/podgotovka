def f(x, y, A):
    if x < y and A == 13:
        return 1
    if x > y or A != 13:
        return 0
    return f(x - 3, y, A + 1) + f(x * (-3), y, A + 1)

print(f(333, 0, 0))