def f(A):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (((x + 2) <= 50) or (y < (x + 10)) or (x >= A))  == 0:
                return False
    return True

for A in range(10000):
    if f(A):
        print(A)
