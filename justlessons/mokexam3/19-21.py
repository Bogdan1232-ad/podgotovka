def f(s1, s2, c, win):
    if s1 + s2 >= 127:
        return c in win
    if c > max(win):
        return 0
    moves = [f(s1 + 2, s2, c + 1, win), f(s1, s2 + 2, c + 1, win), f(s1 * 3, s2, c + 1, win), f(s1, s2 * 3, c + 1, win)]
    if c % 2 != max(win) % 2:
        return any(moves)
    else:
        return all(moves)

for s in range(1, 123):
    # if f(2, s, 0, [2]):
    #     print(s)
    if f(2, s, 0, [1]) == 0 and f(2, s, 0, [3]) == 1:
        print(s)
    # if f(2, s, 0, [2, 4]) == 1 and f(2, s, 0, [2]) == 0:
    #     print(s)