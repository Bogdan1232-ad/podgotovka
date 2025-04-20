def f(s, c):
    if s >= 73: return c % 2 == 0
    if c == 0: return 0
    moves = [f(s + 1, c - 1), f(s + 3, c - 1), f(s * 2, c - 1)]
    return any(moves) if (s + 1) % 2 == 0 else all(moves)


print('19.', [i for i in range(1, 73) if f(i, 2) == 1])
print('20.', [i for i in range(1, 73) ])

