def delll(num, num2):
    if num % num2 == 0:
        return True
    return False

def f(A):
    for x in range(1, 1000):
        u = delll(A, 12) and delll(530, x) <= ((not delll(A, x)) <= (not(delll(170, x))))
        if not u:
            return False
    return True

cnt = 0
for A in range(1, 1001):
    if f(A):
        cnt += 1
print(cnt)