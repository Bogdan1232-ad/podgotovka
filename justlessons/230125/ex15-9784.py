def f(a):
    for x in range(1, 100):
        for y in range(1, 100):
            if not((x * y < a) or (x < y) or (9 < x)):
                return False
    return True

for a in range(1, 100):
    if f(a):
        print(a)
        break