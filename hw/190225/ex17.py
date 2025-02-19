with open('17.txt') as file:
    data = [int(i) for i in file]

ans = []
max_50 = max([i for i in data if str(i)[-2:] == '50'])

for i in range(len(data) - 2):
    a1 = data[i]
    a2 = data[i + 1]
    a3 = data[i + 2]

    u1 = len(str(abs(a1))) == 5
    u2 = len(str(abs(a2))) == 5
    u3 = len(str(abs(a3))) == 5
    uu1 = ((a1 != a2 )and (a2 != a3) and (a1 != a3))
    uu2 = (u1 + u2 + u3) == 3
    uu3 = (a1 + a2 + a3) <= max_50
    if uu1 and uu2 and uu3:
        ans.append(a1 + a2 + a3)
print(len(ans), max(ans))
