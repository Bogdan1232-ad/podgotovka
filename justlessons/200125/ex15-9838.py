def f(A):
    for x in range(0, 100):
        for y in range(0, 100):
            if not((x + 2*y > A) or (y < x) or (x < 30)):
                return False
    return True
for A in range(0, 100)[::-1]:
    if f(A):
        print(A)