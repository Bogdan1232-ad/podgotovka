from itertools import product

def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

results = []

for r in range(8):
    for p in product('0123456789', repeat=r):
        for i in '0123456789':
            number_str = '12' + ''.join(p) + '567' + i
            number = int(number_str)
            if number <= 10**10 and number % 7777 == 0:
                divisors = get_divisors(number)
                min_divisor = min(divisors)
                max_divisor = max(divisors)
                if (min_divisor + max_divisor) % 2 == 1:
                    results.append((number, number // 7777))

results.sort()

for num, quotient in results:
    print(num, quotient)