def f(x, y, c):
    if x + y >= 44: return c % 2 == 0
    if c == 0: return False
    moves = [f(x + y, y, c - 1), f(x, x + y, c - 1)]
    return any(moves) if (c - 1) % 2 == 0 else all(moves)
print('19.', [s for s in range(1, 44) if f(11, s, 1)])
print('20.', [s for s in range(1, 44) if f(11, s, 2) and not f(11, s, 1)])
print('21', [s for s in range(1, 44) if f(s, s, 3)])