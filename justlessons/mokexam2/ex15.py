def f(A):
    for x in range(1, 500):
        for y in range(1, 500):
            if not((x - 3 * y < A) or (y > 400) or (x > 56)):
                return False
    return True

for a in range(1000):
    if f(a):
        print(a)
        break