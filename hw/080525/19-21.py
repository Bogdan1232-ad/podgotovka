def f(x, c):
    if x >= 348: return c % 2 == 0
    if c == 0: return False
    moves = [f(x + 2, c - 1), f(x + 4, c - 1), f(x * 3, c - 1)]
    return any(moves) if (c - 1) % 2 == 0 else all(moves)

print('19.', [i for i in range(1, 348) if f(i, 2) == 1])
print('20.', [i for i in range(1, 348) if f(i, 3) == 1 and f(i, 1) == 0])
print('20.', [i for i in range(1, 348) if f(i, 4) == 1 and f(i, 2) == 0])