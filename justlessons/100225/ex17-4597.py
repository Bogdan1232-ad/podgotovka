from itertools import repeat

with open('17_4597.txt') as file:
    data = [int(i) for i in file]

minn = min(data)

l = []
for i in range(1, len(data)):
    a1 = data[i - 1]
    a2 = data[i]
    if a1 % 117 == minn or a2 % 117 == minn:
        l.append(a1 + a2)

print(len(l), max(l))

