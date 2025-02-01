def f(A):
    for x in range(1, 100):
        for y in range(1, 100):
            if not ((x + y <= 22) or (y <= (x-6)) or (y>=A)):
                return False
    return True

for A in range(0, 1000):
    if f(A):
        print(A)