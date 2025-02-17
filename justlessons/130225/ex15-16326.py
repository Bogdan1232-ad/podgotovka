def dell(x, y):
    return x % y == 0

def f(A):
    for x in range(1, 10000):
        d = (not dell(x, A)) <= (dell(x, 14) <= (not dell(x, 4)))
        if not(d):
            return False
    return True

for A in range(1, 10000):
    if f(A):
        print(A)