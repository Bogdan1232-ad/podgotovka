def dell(x, d):
    return x % d == 0

def f(A):
    for x in range(-10, 500):
        for y in range(-10, 500):
            f = ((x & 500 != 0) and (x & 200 == 0)) <= (not(x & A == 0))
            if not(f):
                return False
    return True

l = []
for A in range(1, 1000):
    if f(A):
        print(A)
        break

