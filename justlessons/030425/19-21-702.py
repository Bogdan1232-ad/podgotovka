def f(s, c):
    if s >= 36 and s <= 85:
        return c % 2 == 0
    if s > 85:
        return c % 2 == 1
    if c == 0:
        return False
    moves = [f(s + 2, c - 1),
             f(s * 3, c - 1)]
    return any(moves) if (c - 1) % 2 == 0 else all(moves)

for c in range(1, 10):
    print(f(6, c))