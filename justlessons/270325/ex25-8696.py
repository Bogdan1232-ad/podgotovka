def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

def M(num):
    summ = 0
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            summ += i
            summ += (num // i)
    if is_prime(num):
        return 0
    return summ

cou = 0
for i in range(1273547, 10**99):
    if is_prime(M(i) % 100_000) and M(i) != 0:
        print(i, M(i))
        cou += 1
    if cou == 5:
        break