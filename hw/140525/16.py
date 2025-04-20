from functools import lru_cache

@lru_cache()
def f(n):
	if n >= 10000:
		return n
	if n < 10_000 and n % 2 == 0:
		return f(n + 1) + n ** 2 - 3 * (n - 1)
	if n < 10_000 and n % 2 != 0:
		return f(n + 2) + 5 * n - (n - 1)

for n in range(102)[::-1]:
	f(n)

print(f(90) - f(99))
