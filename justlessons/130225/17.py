with open('17_7716.txt') as file:
    data = [int(i) for i in file]

def dell(x, y):
    for i in str(x):
        if int(i) % 2 != y:
            return False
    return True

max_nechet = max([i for i in data if dell(i, 0)])
ans = []

cou = 0
for i in range(len(data) - 2):
    n1, n2= data[i: i + 2]
    if n1 + n2 > max_nechet:
        u1 = dell(n1, 1)
        u2 = dell(n2, 1)
        if u1 or u2:
            cou += 1
            ans.append(n1 + n2)
print(cou, max(ans))