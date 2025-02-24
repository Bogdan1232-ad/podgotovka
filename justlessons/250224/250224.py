with open('17_18582.txt') as file:
    data = [int(i) for i in file]

ans = []
min_el = str(min(data))[-1]

for i in range(len(data) - 2):
    a1 = data[i]
    a2 = data[i + 1]
    a3 = data[i + 2]

    u1 = a1 < 0
    u2 = a2 < 0
    u3 = a3 < 0

    if u1 + u2 + u3 >= 2:
        if str(a1 + a2 + a3)[-1] == min_el:
            ans.append(abs(a1 + a2 + a3))

print(len(ans), max(ans))