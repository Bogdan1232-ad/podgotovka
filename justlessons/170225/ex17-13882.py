with open('17_13882.txt') as file:
    data = [int(i) for i in file]

max_401 = max([i for i in data if i % 401 == 0])
ans = []

for i in range(len(data) - 2):
    a1 = data[i]
    a2 = data[i + 1]
    a3 = data[i + 2]

    u1 = sum(map(int, str(a1)))
    u2 = sum(map(int, str(a2)))
    u3 = sum(map(int , str(a3)))
    if u1 != u2 and u2 != u3 and u1 != u3:
        if (a1 + a2 + a3) > max_401:
            ans.append(a1 + a2 + a3)
print(len(ans), min(ans))

