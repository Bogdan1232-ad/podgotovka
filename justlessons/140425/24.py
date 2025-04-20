from string import ascii_uppercase

with open("24_21421.txt") as file:
    data = file.readline()

for i in ascii_uppercase:
    data = data.replace()

l = set()
for i in data:
    i = i.strip('0')
    if int(i) % 2 == 0:
        l.add(i)

print(max(l, key=len))
