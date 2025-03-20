def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for n in range(4, 1000):
    s = '>' + 25 * '0' + n * '1' + 25 * '2'
    while '>1' in s or '>2' in s or '>0' in s:
        s = s.replace('>1', '22>', 1)
        s = s.replace('>2', '2>', 1)
        s = s.replace('>0', '1>', 1)
    s = s.replace('>', '')
    if is_prime(sum(map(int, s))):
        print(n)
        break