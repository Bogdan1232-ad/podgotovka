def f(n):
    if n > 3000:
        return n
    if n % 2 == 0:
        next_n = n + 1
        k = (3001 - next_n) // 2
        f_next = next_n + 4 * k
        return n + f_next + 1
    else:
        k = (3001 - n) // 2
        return n + 4 * k


print(f(40) - f(43))
