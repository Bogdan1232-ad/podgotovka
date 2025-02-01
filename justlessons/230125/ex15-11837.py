def f(a):
    for x in range(0, 1000):
        for y in range(0, 1000):
            if not((x**2 + y**2 > 1024 - x) or (y < -2 * x + a)):
                return False
    return True

for a in range(0, 100):
    if f(a):
        print(a)
        break