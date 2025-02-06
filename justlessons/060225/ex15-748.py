from itertools import combinations


def f(x):
    P = 44 <= x <= 49
    Q = 28 <= x <= 53
    A = A1 <= x <= A2
    return (A <= P) or Q

ans = []
line = [i/10 for i in range(280, 530)]

for A1, A2 in combinations(line, 2):
    if all(f(x) == True for x in line):
        ans.append(A2-A1)

print(max(ans))