for a in [0, 1]:
    for b in [0, 1]:
        for c in [0, 1]:
            f = a and (not b) or c
            if f == 1:
                print(b, c, a, int(f))