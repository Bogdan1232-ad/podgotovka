for x in range(2):
    for y in range(2):
        for z in range(2):
            u = (not(x == (y <= z)))
            print(y, x, z, int(u))