from itertools import permutations

graph = 'AB AC AD BC CD CE DE FE FG DF GE'.split()
matrix = '347 3456 1245 1237 236 25 14'

for i in permutations('ABCDFGE'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
