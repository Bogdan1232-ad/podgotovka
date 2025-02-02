from functools import lru_cache

@lru_cache(None)
def convert(x):
    result = []
    while x > 0:
        result.append(x % 10)
        x //= 10
    return result
def f(x, y):
    if x>y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 2, y) + f(max(convert(x)) + x, y)
print(f(32, 55) * f(55, 76))