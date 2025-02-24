def f(A):
    for x in range(90, 101):
        u = (not(x & 79 == 0)) and ((x & 31 == 0) <= (not(x & A == 0)))
        if not(u):
            return False
    return True

for A in range(1000):
    if f(A):
        print(A)
        break