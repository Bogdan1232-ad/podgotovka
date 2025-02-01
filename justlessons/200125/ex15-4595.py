def f(A):
    for x in range(1, 1000):
        if not(((x%2 == 0) <= (not x%3 == 0)) or (x + A >= 80)):
            return False
    return True

for A in range(-1000, 1000):
    if f(A):
        print(A)
        break
