def f(s, c):
    if s <= 87: return c % 2 == 0
    if c < 0: return False
    moves = [f(s - 2, c - 1), f(s // 2, c - 1)]
    return any(moves) if (c - 1) % 2 == 0 else all(moves)

print('19.', [i for i in range(88, 200) if f(i, 2) and not f(i, 1)])
print('20.', [i for i in range(88, 200) if f(i, 3) and not f(i, 1)])
print('21.', [i for i in range(88, 200) if f(i, 4) and not(f(i, 2))])