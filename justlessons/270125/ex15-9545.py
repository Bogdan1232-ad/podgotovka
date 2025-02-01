def dell(x, d):
    return x % d == 0

def f(A):
    for x in range(-10, 500):
        for y in range(-10, 500):
            f = (((dell(x, 10) and dell(x, 26)) and (x >= 300)) <= (A <= x))
            if not(f):
                return False
    return True

l = []
for A in range(1, 1000):
    if f(A):
        print(A)
        l.append(A)

print(max(l))