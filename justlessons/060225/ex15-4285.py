from itertools import combinations

def f(x):
    P = 25 <= x <= 240
    R = 270 <= x <= 340
    Q = 175 <= x <= 300
    A = A1 <= x <= A2
    return (Q <= P) or ((not A) <= R)

line = [i/10 for i in range(2500, 3400)]
ans = []

for A1, A2 in combinations(line,  2):
    if all(f(x) for x in line):
        ans.append(A2 - A1)

print(min(ans))