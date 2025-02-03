from itertools import combinations

def f(x):
    P = 23 <= x < 45
    Q = 34 <= x <= 56
    A = A1 <= x <= A2

ans = []
line = [i/10 for i in range(23*10, 56*10)]

for i in