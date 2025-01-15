from itertools import permutations


graph = 'AG AF GF FH HE HC ED DG BC BE BD'.split()
matrix = '234 157 147 138 268 58 23 456'.split()

for i in permutations('ABCDEFHG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
