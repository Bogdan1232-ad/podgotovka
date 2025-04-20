def f(A):
    for x in range(1000):
        for y in range(1000):
            if not (((A < x) or (x ** 2 - 7 * x + 10 > 0)) and ((A >= y) or (y ** 2 + 7 * y + 12 > 0))):
                return False
    return True


cnt = 0
for A in range(-1000, 1000):
    if f(A):
        cnt += 1
print(cnt)
