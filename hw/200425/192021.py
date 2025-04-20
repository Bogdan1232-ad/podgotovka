def f(x, y, s):
    if x + y <= 100: return s % 2 == 0
    if s == 0: return False
    moves = [f(x - 3, y - 3, s - 1), f(x // 2, y, s - 1), f(x, y // 2, s - 1)]
    return any(moves) if (s - 1) % 2 == 0 else all(moves)

print('19.', [s for s in range(53, 100) if f(48, s, 2)])
print('20.', [s for s in range(53, 100) if f(s, 48, 3) and not(f(s, 48, 1))])
