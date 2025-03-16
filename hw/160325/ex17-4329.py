def get_div(num):
    l = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            l.add(i)
            l.add(num // i)
    l.add(num)
    return l


with open('17_4329.txt') as file:
    data = [int(i) for i in file]

for i in data:
    if len(get_div(i)) == 30:
        max_divs = i
divs_760 = get_div(760)
# 30
print(divs_760)


def matc(x):
    cou = 0
    for i in get_div(x):
        if i in divs_760:
            cou += 1
    return cou


ans = []
for i in range(len(data) - 1):
    a1 = data[i]
    a2 = data[i + 1]

    if matc(a1) >= 3 and matc(a2) >= 3:
        ans.append(max(matc(a1), matc(a2)))

print(len(ans), max(ans))
