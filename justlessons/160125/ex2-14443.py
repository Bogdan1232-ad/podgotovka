from itertools import permutations

graph = 'AB AD AE BD BC DE DF DC CB CF FG GE'.split()
matrix = '23567 145 146 23 127 137 156'.split()

print(*range(1, 8))
for i in permutations('ABCDEFG'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)
