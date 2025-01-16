from itertools import permutations

graph = 'AB AG AV BV BG VD GD DE DZ EZ EQ QG QZ DZ'.split()
matrix = '256 145 478 237 126 158 348 2367'.split()

print(*range(1, 8))
for i in permutations('ABVGDEZQ'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
