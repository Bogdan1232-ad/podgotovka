from itertools import permutations

graph = 'FD FB DA DC BA BE AC AG CH HG GE HC'.split()
matrix = '36 478 178 258 46 158 23 2346'.split()

print(*range(8))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)